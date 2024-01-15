import PySimpleGUI as sg
layout=[
    [sg.Text('-Rolands-'),sg.InputText(key='-Rolands-', enable_events=True) ],
    [sg.Text('-Rolands-'),sg.InputText(key='-Rolands-', enable_events=True) ],
    [sg.Button('OK')],
    [sg.Text('', key='-OUTPUT-')]
]
window=sg.Window('Skola', layout)
while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED:
        break
     window[''].update({values['']} {values['']}"),
else:
    sg.popup_error('Lūdzu, ievadiet vārdu un uzvārdu.')