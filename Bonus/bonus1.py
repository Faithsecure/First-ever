import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button1 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button],
                           [label2, input2, choose_button1],
                           [compress_button]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["Choose"].split(";")
    folder = values["Choose0"]
    make_archive(filepaths, folder)

window.close()