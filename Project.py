import pandas as pd
from pandas import read_json, read_csv

#Convert Json to CSV file

workstationFile = read_json('workstation_in_final.json')
workstationFile.columns = ['workstation_id', 'workstation_os', 'workstation_vendor']
workstationFile.to_csv('workstation.csv', index=False)
workstationCSVFile = read_csv('workstation.csv')

#Read CSV input files

userInfoFile = pd.read_csv('user_in.csv')
winEventFile = pd.read_csv('winEvent.csv')

#Merge user_info and win_events datas to one CSV file(winUserEvents)

winEventFile = winEventFile.dropna(axis=1)
joinUserToEvent = userInfoFile.merge(winEventFile, on='user_id')
joinUserToEvent.to_csv('winUserEvents.csv', index=False)

#Merge workstation_info to winUserEvents(Result)

winUserEventsFile = read_csv('winUserEvents.csv')
joinJson = winUserEventsFile.merge(workstationCSVFile)
joinJson.to_csv('winUserEvents.csv', index=False)
