
import os, shutil, re

types = {"text":"txt",
         "pdf":"pdf",
         "audio":"mp3",
         "latex":"tex",
         "movie and show":"srt",
         "image":["png", "jpg","jpeg", "bmp", "gif", "raw"],
         "video":["mov", "mp4", "avi", "flv","mkv"],
         "document":["doc", "docx"],
         "spreadsheet":["xls", "xlsx"],
         "presentation":["ppt", "pptx"],
         "code":["py", "cs", "js", "php", "html", "sql", "css"],
         "executable":["exe", "msi"],
         "compressed":["rar","zip"]
            }

showMovieRegex = re.compile(r'\d{3,4}[pP]|[sS]\d{1,2}[eE]\d{1,2}') 

def makeFolder(foldername,path): 
    os.chdir(path)
    if os.path.exists(foldername) == True: 
        return os.getcwd() + os.sep + str(foldername) 
    else:
        os.mkdir(str(foldername)) 
        return os.getcwd() + os.sep + str(foldername)

def moveNewFolder(srcPath,pathNewFolder): 
    try:
        shutil.move(srcPath, pathNewFolder)
    except:
        pass

def folderName(name): 
    if showMovieRegex.search(name): 
        return 'movie and show'
    else:
        for value in types.items(): 
            if name[name.rindex('.')+1:] in value[1]:
                return value[0] 
        return 'other'


def organizer(paths): 
    for path in paths:
        with os.scandir(path) as it:
            for entry in it:
               
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
                    try:
                        moveNewFolder(entry.path, makeFolder(folderName(entry.name),path)) 
                    except:
                        pass
