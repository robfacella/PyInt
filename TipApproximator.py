print('Calculates expected wages based on hours.')
print('Expecting 4 to 5 dollars in tips per hour.')
wages = 6.0
high = 5.0
low = 4.0

hours = float(input('Enter hours worked for the week: '))
print(' ')
salary = wages * hours
print('Wages should be ', format(salary, '.2f'))

high = high * hours
low = low * hours
print('Expect ', format(low, '.2f'), ' to ', format(high, '.2f'), ' , in tips, to be claimed on paycheck.')
print(' ')
lowT = low + salary
highT = high + salary
print('Gross reported pay will be', format(lowT, '.2f'), ' to ', format(highT, '.2f'))
#Taxed roughly 16% of the Gross
lowT = salary - (lowT * 0.16)
highT = salary - (highT * 0.16)
print('Check after tax should be ', format(lowT, '.2f'), ' to ', format(highT, '.2f'))
lowT = lowT + low
highT = highT + high
print('Reported take-home after tax ', format(lowT, '.2f'), ' to ', format(highT, '.2f'))
