import os, shutil, re

path = 'C:\\Users\\'
types = {'txt':'text',
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
show_movie_regex = re.compile(r'\d{3,4}[pP]|[sS]\d{1,2}[eE]\d{1,2}')

def make_folder(foldername):
    os.chdir(path)
    if os.path.exists(foldername) == True:
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)

def move_to_new_folder(src_path,path_to_new_folder):
    try:
        shutil.move(src_path, path_to_new_folder)
    except:
        pass

def foldername(name,is_file):
    if show_movie_regex.search(name):
        return 'movie and show'
    elif is_file:
        for value in types.keys():
            if name[name.rindex('.')+1:] in value:
                return types[value]
        return 'other'

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.'):
            try:
                move_to_new_folder(entry.path, make_folder(foldername(entry.name,entry.is_file)))
            except:
                pass

""" watchdog """

