import os
import time
from datetime import date

#Creating the folder for the day
year = time.strftime('%y')
month = time.strftime('%m')
day = time.strftime("%d")
today_date = month + '-' + day + '-' + year

def return_word_date():
    word_date  = date(day=int(day), month=int(month), year=int(year)).strftime('%A %B %d,') + " 20" + year
    return word_date

def return_num_date():
    return str(month) + '-' + str(day) + '-' + str(year)

dir = '/Users/andrewkruszka/Desktop/Quotidian/'

#Checking the files
if not os.path.exists(dir + "/" + year):
    os.makedirs(dir + "/" + year)

if not os.path.exists(dir + "/" + year + "/" + month):
    os.makedirs(dir + "/" + year + "/" + month)

if not os.path.exists(dir + "/" + year + "/" + month + "/" + day):
    os.makedirs(dir + "/" + year + "/" + month + "/" + day)
    pdf_path = '/Users/andrewkruszka/Desktop/Quotidian/'+ year + "/" + month + "/" + day + "/"

def get_path():
    return '/Users/andrewkruszka/Desktop/Quotidian/'+ year + "/" + month + "/" + day + "/"