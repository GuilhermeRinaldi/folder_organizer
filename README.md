# Folder Organizer 

![](https://badgen.net/badge/python/3.8.8/blue?icon=v) ![](https://badgen.net/badge/pysimpleGUI/tkinter/blue?icon=v)

------

![1](https://user-images.githubusercontent.com/37752370/147109394-21557ccf-11b1-4f1b-bb1e-f7104a19f7c7.gif)

## Funcionamento

### Identificação e destino de arquivos

O arquivo  `organizer.py` carrega as funções que controlam os destinos e identificação dos arquivos possui uma variavel que carrega um dicionario com a relação **nome da pasta : extenções** onde ficam definidos os destinos para cada tipo de arquivo.

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

Esses botões adicionam caminhos a entrada e são definidos no arquivo `tela.py` por um dicionario que relaciona **Nome : Caminho** 

```python
user = os.getcwd().split("\\")[2] 

btnPath = {'Downloads':'C:/Users/'+ user + '/Downloads',
           'Documents':'C:/Users/'+ user + '/Documents',
           'Desktop':'C:/Users/'+ user + '/Desktop',
           'Pictures':'C:/Users/'+ user + '/Pictures',
           'Videos':'C:/Users/'+ user + '/Videos', 
           'Music':'C:/Users/'+ user + '/Music'}
```

## Utilização

### Caminhos
São aceitos caminhos separados com / ou \\.

### 

## Uso



