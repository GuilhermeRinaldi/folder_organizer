
import PySimpleGUI as sg

from organizer import *

user = os.getcwd().split("\\")[2] # captura o nome de usario do sistema 

btnPath = {'Downloads':'C:/Users/'+ user + '/Downloads',
           'Documents':'C:/Users/'+ user + '/Documents',
           'Desktop':'C:/Users/'+ user + '/Desktop',
           'Pictures':'C:/Users/'+ user + '/Pictures',
           'Videos':'C:/Users/'+ user + '/Videos', 
           'Musicas':'C:/Users/'+ user + '/Musicas'}

listPath = [] # caminhos das pastas que se deseja organizar |

sg.theme("DarkGrey5")

pathSelection =[[sg.Button('Download'), sg.Button('Documents'), sg.Button('Desktop'), sg.Button('Pictures'), sg.Button('Videos'), sg.Button('Musicas')],
                [sg.InputText('C:/Users/'+ user + '/', key='inputPath',size=(39,10), background_color='grey'),sg.FolderBrowse('🔍',font=(2),key='browse'),
                sg.Button('➕',font=(2), key = 'add' ),sg.Button('✖️',font=(2), key = 'del' )]]

pathList = [sg.Listbox(listPath ,expand_x = False, size= (56,5), background_color='grey', key ='listPath')]

actions = [sg.Button('run',expand_x = True,key='run')]

layout = [pathSelection,pathList,actions]

window =sg.Window('Folder organizer',layout)

while True:

    event,values=window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #Preselect path    
    if event in btnPath:
        window['inputPath'].update(btnPath[event])

    # add path in listpath
    if event == 'add':
        listPath.append(values['inputPath'])
        window['listPath'].update(listPath)

    if event == 'del':
        try:
            print(window['listPath'].get_indexes()[0])
            del listPath[window['listPath'].get_indexes()[0]]
            window['listPath'].update(listPath)
            print(listPath)
        except:
            pass

    if event == 'run':
        print(window['listPath'].get_list_values())    
        organizer(window['listPath'].get_list_values())        

window.close()
