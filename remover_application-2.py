import pandas as pd

import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [	[sg.Text('Input Path: Filename.format',font='Arial 18')],
            [sg.Text('e.g. "/Users/jackhobhouse/Expiring-Subscriptions.csv"',font='Arial 18')],
          	[sg.Input(font='Arial 18'), sg.FileBrowse(font='Arial 18')],
            [sg.Text('Output Path: Filename.format',font='Arial 18')],
            [sg.Text('e.g. "/Users/jackhobhouse/Expiring-Subscriptions-2.csv"',font='Arial 18')],
          	[sg.Input(font='Arial 18'), sg.FileBrowse(font='Arial 18')],
	  		    [sg.Submit(font='Arial 18'), sg.Cancel(font='Arial 18')]]

window = sg.Window('Duplicates Remover',layout)

button, values = window.Read()

window.close()

Column = 'Shipment ID'

data = pd.read_excel(values[0])

data.sort_values(Column, inplace = True)

data.drop_duplicates(subset = Column,
                     keep = 'first', inplace = True)


data.to_excel(values[1], index=False)


sg.Popup('All duplicates have now been removed',font='Arial 20')
