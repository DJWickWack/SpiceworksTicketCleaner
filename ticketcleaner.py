import datetime
import pandas as pd
import openpyxl

df = pd.read_csv('ticket_export.csv')
notneeded= ['Ticket Number','Summary','Description','Organization Host','Organization Name','Time Spent','Link to Ticket','System','Due On','Priority','Status']
for x in notneeded:
    del df[x]

totime=['Closed On', 'Created On']
for x in totime:
    df[x]=pd.to_datetime(df[x])

year=datetime.datetime.now().year

currentyeardf=df[(df['Created On'].dt.date>datetime.date(year,1,1)) & (df['Created On'].dt.date<datetime.date(year,12,1))]

currentyeardf['Created On'] = currentyeardf['Created On'].apply(lambda a: pd.to_datetime(a).date())
currentyeardf['Closed On'] = currentyeardf['Closed On'].apply(lambda a: pd.to_datetime(a).date())
currentyeardf.to_excel("currentcleanedtickets.xlsx")