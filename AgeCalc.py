from datetime import date

#Calculates years old today based on Date of Birth
def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
print()
print(calculate_age(date(2003,12,25)))
print(calculate_age(date(1996,6,27)))
print()
