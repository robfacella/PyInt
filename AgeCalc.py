from datetime import date

#Calculates years old today based on Date of Birth
def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
print()
#print(calculate_age(date(2003,12,25)))
#print(calculate_age(date(1996,6,27)))
year = int(input('Enter your birth year: '))
month = int(input('[1-12] Enter your birth month: '))
day = int(input('[1-31] Enter your birthday: '))
dob = date(year,month,day)
print('You are ', calculate_age(dob), ' years old.')
#print('You were born on ', dob.month, ' / ', dob.day, ' of ', dob.year )
#print(dob)
#dates are stored as <yyyy-mm-dd>

#print("I need a way to store and recall dates. Figure out database and python formatting for it..")
#Thinking MongoDB
#pip install pymongo
#from pymongo import MongoClient
