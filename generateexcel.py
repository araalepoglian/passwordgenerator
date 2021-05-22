import random
import string
import pandas as pd

print ('4 letter word password generator')

file ='list.xlsx'
data = pd.ExcelFile(file)
df = data.parse(pass)
df.info
df.head(10)
