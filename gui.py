import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
main_window_layout = [  [sg.Titlebar(title='display-input-switcher')],
                        [sg.Text('Detected monitors:')],
                        [sg.Text('Acer'), sg.Text('Gigabyte')],
                        [sg.Text('Detected inputs:')],
                        [sg.Radio('HDMI1', group_id='display_input_1'), sg.Radio('HDMI1', group_id='display_input_2')],
                        [sg.Radio('HDMI2', group_id='display_input_1'), sg.Radio('HDMI2', group_id='display_input_2')],
                        [sg.Radio('DP1', group_id='display_input_1'), sg.Radio('DP1', group_id='display_input_2')]
]

# Create the Window
window = sg.Window('display-input-switcher', main_window_layout)

# Event Loop to process "events" and get the "values" of the inputs
running : bool = True
while running:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        running = False
    print('You entered ', values[0])

window.close()

### TODO:
### minimalize to tray on close
### settings panel with option to turn this behavior off, also button ot exit
### Change layout to table and populate cells with detected settings
### add panel to access other monitor settings as audio, brightness, mode or something like that
### app disapear after losing focus