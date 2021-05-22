
import pandas as pd

print ('4 letter word password generator')

file ='list.xlsx'
data = pd.ExcelFile(file)
df = data.parse(sheet1)
df.info
df.head(10)
