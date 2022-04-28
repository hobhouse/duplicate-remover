import pandas as pd

import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [	[sg.Text('Input file type',font='Arial 18')],
            [sg.InputCombo(('csv', 'excel'), size=(5, 1),font='Arial 18')],
            [sg.Text('Input Path: Filename.format',font='Arial 18')],
            [sg.Text('e.g. "/Users/jackhobhouse/Expiring-Subscriptions.csv"',font='Arial 18')],
          	[sg.Input(font='Arial 18'), sg.FileBrowse(font='Arial 18')],
            [sg.Text('Output Path: Filename.format',font='Arial 18')],
            [sg.Text('e.g. "/Users/jackhobhouse/Expiring-Subscriptions-2.csv"',font='Arial 18')],
          	[sg.Input(font='Arial 18'), sg.FileBrowse(font='Arial 18')],
            [sg.Text('Column to sort by',font='Arial 18')],
            [sg.Text('e.g. "id"',font='Arial 18')],
          	[sg.Input(font='Arial 18')],
	  		    [sg.Submit(font='Arial 18'), sg.Cancel(font='Arial 18')]]

window = sg.Window('Duplicates Remover',layout)

button, values = window.Read()

window.close()


if values[0] == 'csv':
  data = pd.read_csv(values[1])
elif values[0] == 'excel':
  data = pd.read_excel(values[1])

data.sort_values(values[3], inplace = True)

data.drop_duplicates(subset =values[3],
                     keep = 'first', inplace = True)

if values[0] == 'csv':
  data.to_csv(values[2], index=False)
elif values[0] == 'excel':
  data.to_excel(values[2], index=False)


sg.Popup('All duplicates have now been removed',font='Arial 20')
