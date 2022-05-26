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

## 1. Estructura del repositorio

:open_file_folder:
:page_with_curl:
:clipboard:


:package:TG_Audio_Inteligente
├── :clipboard:config.json5
├── :open_file_folder:Dataset
│   ├── :page_with_curl:div_audio.py
│   ├── :page_with_curl:mix_audio.py
│   ├── :page_with_curl:dataset_list.py
│   ├── :clipboard:train_list_dataset.txt
│   ├── :clipboard:validation_list_dataset.txt
│   └── :clipboard:test_list_dataset.txt
├── :open_file_folder:Perceptron
│   ├── :page_with_curl:generator.py
│   ├── :page_with_curl:model.py
│   └── :page_with_curl:train.py
└── :open_file_folder:CRN
    ├── :open_file_folder:config
    │   ├── :open_file_folder:train
    │   │   └── :clipboard:baseline_model.json5
    │   └── :open_file_folder:inference
    │       └── :clipboard:basic.json5
    ├── :open_file_folder:dataset
    ├── :open_file_folder:inferencer
    ├── :open_file_folder:model
    ├── :open_file_folder:trainer
    ├── :open_file_folder:util
    ├── :page_with_curl:inference.py
    └── :page_with_curl:train.py

- :package:TG_Audio_Inteligente
  - :clipboard:[config.json5](config.json5)
  - :open_file_folder:Dataset
    - :page_with_curl:div_audio.py
    - :page_with_curl:mix_audio.py
    - :page_with_curl:dataset_list.py
    - :clipboard:train_list_dataset.txt
    - :clipboard:validation_list_dataset.txt
    - :clipboard:test_list_dataset.txt
  - :open_file_folder:Perceptron
    - :page_with_curl:generator.py
    - :page_with_curl:model.py
    - :page_with_curl:train.py
  - :open_file_folder:CRN
    - :open_file_folder:config
      - :open_file_folder:train
        - :clipboard:baseline_model.json5
      - :open_file_folder:inference
        - :clipboard:basic.json5
    - :open_file_folder:dataset
      -:open_file_folder:inferencer
      - :open_file_folder:model
      - :open_file_folder:trainer
      - :open_file_folder:util
      - :page_with_curl:inference.py
      - :page_with_curl:train.py
