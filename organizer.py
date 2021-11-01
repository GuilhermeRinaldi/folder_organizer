
import os, shutil, re, time # caminhos, pastas e arquivos | criar e mover | regex |

types = {"txt":"text",
         "pdf":"pdf",
         "mp3":"audio",
         "tex":"latex",
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

show_movie_regex = re.compile(r'\d{3, 4}[pP]|[sS]\d{1,2}[eE]\d{1,2}') #regex para identificar séries e filmes | 

def make_folder(foldername,path): # cria pastas |
    os.chdir(path)
    if os.path.exists(foldername) == True: # verifica a existencia da pasta |
        return os.getcwd() + os.sep + str(foldername) # retorna o caminho da pasta (os.sep = \) |
    else:
        os.mkdir(str(foldername)) # cria pasta caso nao exista |
        return os.getcwd() + os.sep + str(foldername)

def move_to_new_folder(src_path,path_to_new_folder): # move os arquivos para as suas pastas |
    try:
        shutil.move(src_path, path_to_new_folder)
    except:
        pass

def foldername(name): # identifica a pasta para qual deve ir |
    if show_movie_regex.search(name): # verfica se esta dentro do regex 
        return 'movie and show'
    else:
        for value in types.items(): 
            if name[name.rindex('.')+1:] in value[1]: # separa a extensão e associa a uma pasta de types |
                return value[0] # retorna a pasta |
        return 'other'


def organizer(paths): 
    for path in paths:
        with os.scandir(path) as it: # lista as pastas e arquivos do path | 
            for entry in it:
                if not entry.name.startswith('.'): # ignora pastas ocultas |
                    try:
                        move_to_new_folder(entry.path, make_folder(foldername(entry.name),path)) 
                    except:
                        pass
