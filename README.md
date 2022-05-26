# Audio inteligente: reducción de ruido de fondo con inteligencia artificial

### Pontificia Universidad Javeriana
### Trabajo de Grado
### Departamento de Electrónica
### Juan Camilo Sarmiento Peñuela


En este repositorio se encuentra el código implementado durante el desarrollo
del trabajo de grado Audio inteligente: reducción de ruido de fondo con
inteligencia artificial, y también se encuentran los modelos entrenados y los
resultados obtenidos. A continuación se describen los contenidos del
repositorio, y cómo utilizar el código para entrenar los modelos y/o
utilizarlos.

                   Este es un test


## 1. Estructura del repositorio

- :package:[TG_Audio_Inteligente](https://github.com/juancas9812/TG_Audio_Inteligente)
  - :clipboard:[config.json5](config.json5)
  - :open_file_folder:[Dataset](Dataset)
    - :page_with_curl:[div_audio.py](Dataset/div_audio.py)
    - :page_with_curl:[mix_audio.py](Dataset/mix_audio.py)
    - :page_with_curl:[dataset_list.py](Dataset/dataset_list.py)
    - :clipboard:[train_list_dataset.txt](Dataset/train_list_dataset.txt)
    - :clipboard:[validation_list_dataset.txt](Dataset/validation_list_dataset.txt)
    - :clipboard:[test_list_dataset.txt](Dataset/test_list_dataset.txt)
  - :open_file_folder:[Perceptron](Perceptron)
    - :page_with_curl:[generator.py](Perceptron/generator.py)
    - :page_with_curl:[model.py](Perceptron/model.py)
    - :page_with_curl:[train.py](Perceptron/train.py)
  - :open_file_folder:[CRN](CRN)
    - :open_file_folder:[config](CRN/config)
      - :open_file_folder:[train](CRN/config/train)
        - :clipboard:[baseline_model.json5](CRN/config/train/baseline_model.json5)
      - :open_file_folder:[inference](CRN/config/inference)
        - :clipboard:[basic.json5](CRN/config/inference/basic.json5)
    - :open_file_folder:[dataset](CRN/dataset)
    - :open_file_folder:[inferencer](CRN/inferencer)
    - :open_file_folder:[model](CRN/model)
    - :open_file_folder:[trainer](CRN/trainer)
    - :open_file_folder:[util](CRN/util)
    - :page_with_curl:[inference.py](CRN/inference.py)
    - :page_with_curl:[train.py](CRN/train.py)
