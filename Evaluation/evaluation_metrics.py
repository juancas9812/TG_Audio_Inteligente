import numpy as np
import torch
from pesq import pesq
from pystoi.stoi import stoi


def SNR(x_sig, y_sig):
    """
        Compute SNR(signal to noise ratio)
        x: enhanced signal
        y: original clean signal
    """
    x = torch.from_numpy(x_sig)  # numpy crashes so use pytorch tensor
    y = torch.from_numpy(y_sig)  # numpy crashes so use pytorch tensor
    ref = torch.pow(y, 2)
    if len(x) == len(y):
        a = x-y
        diff = torch.pow(a, 2)
    else:
        stop = min(len(x), len(y))
        diff = torch.pow(x[:stop]-y[:stop], 2)
    ratio = torch.sum(ref)/torch.sum(diff)
    value = 10*torch.log10(ratio)
    return value


def SDR(reference, estimation):
    """
    Scale-Invariant Signal-to-Distortion Ratio (SI-SDR)

    Args:
        reference: numpy.ndarray, [..., T]
        estimation: numpy.ndarray, [..., T]
    Returns:
        SI-SDR
    [1] SDR– Half- Baked or Well Done?
    http://www.merl.com/publications/docs/TR2019-013.pdf
    """
    estimation, reference = np.broadcast_arrays(estimation, reference)
    reference_energy = np.sum(reference ** 2, axis=-1, keepdims=True)

    # This is $\alpha$ after Equation (3) in [1].
    optimal_scaling = np.sum(reference * estimation, axis=-1, keepdims=True) \
        / reference_energy

    # This is $e_{\text{target}}$ in Equation (4) in [1].
    projection = optimal_scaling * reference

    # This is $e_{\text{res}}$ in Equation (4) in [1].
    noise = estimation - projection

    ratio = np.sum(projection ** 2, axis=-1) / np.sum(noise ** 2, axis=-1)
    return 10 * np.log10(ratio)


def STOI(ref, est, sr):
    return stoi(ref, est, sr, extended=False)


def PESQ(ref, est, sr):
    return pesq(sr, ref, est, "wb")
