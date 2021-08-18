
import PySimpleGUI as sg
#set the theme for the screen/window
sg.theme("DarkGrey5")
#define layout
sz=(10,5)
pathSelection =[[sg.Checkbox('Download', key='Download'),sg.Checkbox('Documents', key='Documents'),sg.Checkbox('Desktop', key='Desktop')],
                [sg.Input( size=(39,10) ,background_color='grey'),sg.Button('+',size=(2,1))]]

pathList = [[sg.Listbox(["s","s"],size=(42,5),background_color='grey')]]

actions = [[sg.Button('Uninstall',size=(18,1)),sg.Button('Execute',size=(18,1))]]

config = [[sg.Checkbox('keep executing', disabled=True,key='keepExecuting')]]

layout = [pathSelection,pathList,actions,config]

window =sg.Window("Folder organizer",layout)
event,values=window.read()

window.close()