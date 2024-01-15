
# definēja loga elementus
layout=[
    [sg.Button('klik')]
]
window=sg.Window('Loga nosaukums', layout)

while True:
    event, values=window.read()
    if even==sg.WIN_CLOSED:
        break
    if event=='klik':
        print('Uz pogas tika uzklikstinats!')

    window.close()