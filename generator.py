import random
import string

print('Welcome to the password generator app')

#set length of password
length = int(input('enter the length of the password: '))

#variable for each section
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine all data
alldata = lower + upper + num + symbols

#use random
temp = random.sample(alldata,length)

password = "".join(temp)

print(password)