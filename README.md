<h1 align="center">Folder Organizer</h1> 

![1](https://user-images.githubusercontent.com/37752370/147109394-21557ccf-11b1-4f1b-bb1e-f7104a19f7c7.gif)

![](https://img.shields.io/static/v1?label=python&message=3.8.8&color=blue&style=for-the-badge&logo=PYTHON)
![](https://img.shields.io/static/v1?label=pysimpleGui&message=tkinter&color=yellow&style=for-the-badge&logo=PYTHON)


> Status do Projeto: ✔️ Concluído

### Sumário 

- [Descrição do projeto](#descrição-do-projeto)
- [Layout](#layout)
- [Pré-requisitos](#pré-requisitos)
- [Funcionamento](#funcionamento)
  - [Identificação e destino de arquivos](#identificação-e-destino-de-arquivos)
  - [Botões predefinidos](#botões-predefinidos)
- [Como Usar](#como-usar)
- [Como gerar um executável](#como-gerar-um-executável)
 
## Descrição do projeto 

<p align="justify">
	Organiza arquivos em pastas baseado em suas extensões.
</p>

## Layout 
![janela](https://user-images.githubusercontent.com/37752370/147363118-46f6f3cf-c5f1-44b1-9521-db5feb02e876.png)


## Pré-requisitos

1. [Python](https://www.python.org/downloads/)
	- [PysimpleGui](https://pysimplegui.readthedocs.io/en/latest/)
	- [os](https://docs.python.org/3/library/os.html)
	- [shutil](https://docs.python.org/3/library/shutil.html)
	- [re](https://docs.python.org/3/library/re.html)
	- [pyinstaller(opcional)](https://www.pyinstaller.org/)


## Funcionamento

### Identificação e destino de arquivos

O arquivo  `organizer.py` carrega as funções que controlam os destinos e identificação dos arquivos, possui uma variável que carrega um dicionário com a relação **nome da pasta : extensões** onde ficam definidos os destinos para cada tipo de arquivo.

```python
types = {"txt":"text",
          "pdf":"pdf",
          "mp3":"audio",
          "latex":"tex",
          "srt":"movie and show",
          "image":["png", "jpg","jpeg", "bmp", "gif", "raw"],
          "video":["mov", "mp4", "avi", "flv","mkv"],
          "document":["doc", "docx"],
          "spreadsheet":["xls", "xlsx"],
          "presentation":["ppt", "pptx"],
          "code":["py", "cs", "js", "php", "html", "sql", "css"],
          "executable":["exe", "msi"],
          "compressed":["rar","zip"]
           }
```

Está definido um regex para arquivos de filmes e series `showMovieRegex = re.compile(r'\d{3,4}[pP]|[sS]\d{1,2}[eE]\d{1,2}')` e para retirar esse recurso basta alterar a função de:

```python
def folderName(name): 
    if showMovieRegex.search(name): 
        return 'movie and show'
    else:
        for value in types.items(): 
            if name[name.rindex('.')+1:] in value[1]:
                return value[0] 
        return 'other'
```
Para:
```python
def folderName(name): 
  for value in types.items(): 
      if name[name.rindex('.')+1:] in value[1]:
          return value[0] 
  return 'other'
```

### Botões predefinidos

![botoes](https://user-images.githubusercontent.com/37752370/147113342-e873cc9e-b79b-4741-9eb7-b9163133b53d.png)

Esses botões adicionam caminhos a entrada e são definidos no arquivo `window.py` por um dicionário que relaciona **Nome do botão : Caminho** 

```python
user = os.getcwd().split("\\")[2] 

btnPath = {'Downloads':'C:/Users/'+ user + '/Downloads',
           'Documents':'C:/Users/'+ user + '/Documents',
           'Desktop':'C:/Users/'+ user + '/Desktop',
           'Pictures':'C:/Users/'+ user + '/Pictures',
           'Videos':'C:/Users/'+ user + '/Videos', 
           'Music':'C:/Users/'+ user + '/Music'}
           
pathSelection =[[sg.Button('Downloads'), sg.Button('Documents'), sg.Button('Desktop'), sg.Button('Pictures'), sg.Button('Videos'), sg.Button('Music')],...
```

## Como usar

No terminal, clone o projeto: 

```
git clone https://github.com/GuilhermeRinaldi/folder_organizer
```
Execute o arquivo `window.py`

Ou

Baixe o `folderOrganizer.exe` e execute

## Como gerar um executável
```
pip install pyinstaller
```
Instale o pyinstaller e Execute o comando:

```
pyinstaller --onefile -w window.py
```
O executável vai estár na pasta dist

## Licença 

The [MIT License]() (MIT)

Copyright © 2021 - Folder Organizer
                                                      
