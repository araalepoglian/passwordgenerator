
import pandas as pd

#print ('4 letter word password generator')

filename = "list.xlsx"

df = pd.read_excel(filename, sheet_name = "Sheet1", engine='openpyxl')
df.head()
