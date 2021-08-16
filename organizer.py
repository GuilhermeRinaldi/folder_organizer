
import os, shutil, re, time

paths = ('C:\\Users\\**\\Downloads\\','C:\\Users\\**\\Documents')# caminhos das pastas que se deseja organizar |

types = {'txt':'text', # extensões : pasta | 
         'pdf':'pdf',
         'mp3':'audio',
         'tex':'latex',
         'srt':'movie and show',
         ('png', 'jpg','jpeg', 'bmp', 'gif', 'raw'):'image',
         ('mov', 'mp4', 'avi', 'flv','mkv'):'video',
         ('doc', 'docx'):'document',
         ('xls', 'xlsx'):'spreadsheet',
         ('ppt', 'pptx'):'presentation',
         ('py', 'cs', 'js', 'php', 'html', 'sql', 'css'):'code',
         ('exe', 'msi'):'executable',
         ('rar','zip'):'compressed'}
show_movie_regex = re.compile(r'\d{3,4}[pP]|[sS]\d{1,2}[eE]\d{1,2}') #regex para identificar séries e filmes | 

def make_folder(foldername,path): # cria pastas |
    os.chdir(path)
    if os.path.exists(foldername) == True:
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)

def move_to_new_folder(src_path,path_to_new_folder): # move os arquivos para as suas pastas |
    try:
        shutil.move(src_path, path_to_new_folder)
    except:
        pass

def foldername(name): # identifica a pasta para qual deve ir |
    if show_movie_regex.search(name):
        return 'movie and show'
    else:
        for value in types.keys():
            if name[name.rindex('.')+1:] in value: # separa a extensão do nome do arquivo |
                return types[value]
        return 'other'


while True:
    for path in paths:
        with os.scandir(path) as it: # lista as pastas e arquivos do path | 
            for entry in it:
                if not entry.name.startswith('.'): # ignora pastas ocultas |
                    try:
                        move_to_new_folder(entry.path, make_folder(foldername(entry.name),path)) 
                    except:
                        pass
    time.sleep(1) # gera uma pausa na execusão | 


#### arquivos ou pastas com ponto no nome estão sujeitos a irem para pasta other ####
#### ####
