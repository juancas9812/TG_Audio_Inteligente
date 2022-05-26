# Audio inteligente: reducción de ruido de fondo con inteligencia artificial

### Pontificia Universidad Javeriana - Trabajo de Grado - Ingenieria Electrónica
#### Juan Camilo Sarmiento Peñuela
---

En este repositorio se encuentra el código implementado durante el desarrollo
del trabajo de grado Audio inteligente: reducción de ruido de fondo con
inteligencia artificial, y también se encuentran los modelos entrenados y los
resultados obtenidos. A continuación se describen los contenidos del
repositorio, y cómo utilizar el código para entrenar los modelos y/o
utilizarlos.

## 1. Estructura del repositorio

- :package:[TG_Audio_Inteligente](https://github.com/juancas9812/TG_Audio_Inteligente)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Repositorio
    - :clipboard:[config.json5](config.json5)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Configuracion para códigos dentro de Dataset y Perceptron
    - :open_file_folder:[Dataset](Dataset)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Carpeta con codigos para crear el conjunto de datos
        - :page_with_curl:[div_audio.py](Dataset/div_audio.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #Codigo para dividir audios originales
        - :page_with_curl:[mix_audio.py](Dataset/mix_audio.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Código para mezclar audios de voz y ruido
        - :page_with_curl:[dataset_list.py](Dataset/dataset_list.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Código para porcionar los datos
        - :clipboard:[train_list_dataset.txt](Dataset/train_list_dataset.txt)
        - :clipboard:[validation_list_dataset.txt](Dataset/validation_list_dataset.txt)
        - :clipboard:[test_list_dataset.txt](Dataset/test_list_dataset.txt)
    - :open_file_folder:[Perceptron](Perceptron)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Carpeta con los códigos del primer modelo
        - :page_with_curl:[generator.py](Perceptron/generator.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Generador de datos para el modelo 1
        - :page_with_curl:[model.py](Perceptron/model.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Arquitectura del modelo 1
        - :page_with_curl:[train.py](Perceptron/train.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Entrenamiento del modelo 1
    - :open_file_folder:[CRN](CRN)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Carpeta con los códigos del segundo modelo
        - :open_file_folder:[config](CRN/config)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Configuraciones para entrenamiento y uso del segundo modelo
            - :open_file_folder:[train](CRN/config/train)
                - :clipboard:[baseline_model.json5](CRN/config/train/baseline_model.json5)&nbsp;&nbsp;&nbsp;#Conficuración para entrenamiento del modelo 2
            - :open_file_folder:[inference](CRN/config/inference)
                - :clipboard:[basic.json5](CRN/config/inference/basic.json5)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Configuración para uso del modelo 2
        - :page_with_curl:[inference.py](CRN/inference.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Código para usar el modelo 2
        - :page_with_curl:[train.py](CRN/train.py)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Código para entrenar el modelo 2


## 2. Dependencias
Se deben tener los siguientes modulos de python en el ambiente:
```
Tensorflow
PyTorch
librosa
numpy
pandas
matplotlib
json5
scikit-learn
scipy
pesq
pystoi
```

## 3. Creacion del conjunto de datos
En caso de ya tener los audios de voz y de ruido con longitud de 5s y con el
mismo muestreo ejecutar solamente el código dataset_list.py.

Se debe modificar el archivo [config.json5](config.json5) y colocar las rutas
de las carpetas y metadatos de los audios antes de ejecutar cualquiera de los
códigos en la carpeta [Dataset](Dataset). Una vez modificado el archivo [config.json5](config.json5), ejecutar de la siguiente manera:
```bash
python3 Dataset/dataset_list.py
```
Al correr [dataset_list.py](Dataset/dataset_list.py), la particion del conjunto
de datos es de 70/15/15 por defecto.


## 4. Entrenamiento del modelo 1
Para entrenar el modelo 1 se debe modificar el archivo [config.json5](config.json5)
con la ruta de los audios de mezcla (voz+ruido) y de voz, y adicionalmente, se
debe especificar el número de epochs y el número de neuronas por capa:
```json
"train.py": {
    "mixed_path": "...ruta de audios con mezcla",
    "clean_path": "...ruta de audios de voz",
    "dataset_csv": "...ruta de los metadatos del conjunto/nombre_del_archivo.csv",
    "layers": [100,100,50],
    "epochs": 20
}
```
Para entrenar el modelo ejecutar de la siguiente manera:
```bash
python3 Perceptron/train.py
```

## 5. Entrenamiento del modelo 2
El modelo 2 se basa en el [código](https://github.com/haoxiangsnr/A-Convolutional-Recurrent-Neural-Network-for-Real-Time-Speech-Enhancement) desarrollado por [haoxiangsnr
](https://github.com/haoxiangsnr). Para un mejor entendimiento de este, revisar
el repositorio [A-Convolutional-Recurrent-Neural-Network-for-Real-Time-Speech-Enhancement](https://github.com/haoxiangsnr/A-Convolutional-Recurrent-Neural-Network-for-Real-Time-Speech-Enhancement).

Antes de entrenar el segundo modelo se debe cambiar el parámetro *"root_dir"* por la ruta
al directorio donde se tiene o se guardará el modelo, los parámetros *"dataset_list"*
por la ruta y nombre del archivo de texto que contiene la lista con los audios
para el entrenamiento y validación respectivamente dentro de *"train_dataset"* y
*"validation_dataset"*. Adicionalmente se puede cambiar el número de epochs
modificando el valor del parámetro *"epochs"* dentro de *"trainer"*.

Para entrenar el segundo modelo:
```
python3 CRN/train.py -C CRN/config/train/baseline_model.json5
```
o entrar a la carpeta CRN y ejecutar el archivo [train.py](CRN/train.py)
