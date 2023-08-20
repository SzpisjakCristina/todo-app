import  functions
import PySimpleGUI as sg

# the text before the box
label = sg.Text("Type in a to-do")
# the text box
input_box = sg.InputText(tooltip="Enter to do")
add_button = sg.Button("Add")

# the window + title of the program
window = sg.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()