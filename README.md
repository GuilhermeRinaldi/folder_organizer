# Folder Organizer 

![](https://badgen.net/badge/python/3.8.8/blue?icon=v) ![](https://badgen.net/badge/pysimpleGUI/tkinter/blue?icon=v)

------
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

O 

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

```python
def folderName(name): 
  for value in types.items(): 
      if name[name.rindex('.')+1:] in value[1]:
          return value[0] 
  return 'other'
```

### uso 

![1](https://user-images.githubusercontent.com/37752370/147011877-99b0cd17-d60c-4a95-a20b-8398d3ed6357.gif)

para as edições dos caminhos que determinados arquivos devem ir referente a suas extensões é uma questão de alterar o dicionário types e suas tuplas para as pastas que devem receber o monitoramento alterar paths.

movie and show

acredito que essa pode ser a mais descartável das pastas logo sua retirada pode ser feita alterando a extensão 'srt' em types e retirando a verificação na função foldername.

aviso 

pastas com nome contendo ponto acabam enviadas para pasta other.


paths and extensions

to edit the paths that certain files should go regarding their extensions, it is a matter of changing the types dictionary and its tuples for the folders that should receive the monitoring change paths.

movie and show


I believe this may be the most disposable of folders so its removal can be done by changing the 'srt' extension in types and removing the check in the foldername function.

Notice

folders with name containing dot end up sent to other folder.
