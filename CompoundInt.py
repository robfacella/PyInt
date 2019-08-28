#Compounded Interest (Savings on Student Loans)

#Amount Invested
#Interest per Year
#Interest per Month
#Number of Years
#Number of extra Months
print('Amount you are investing.')
invested = float(input('Principal Investment: '))
print(' ')

print('Input annual percentage rate ')
print('Enter "10" for 10% (Do not add the "%" symbol or divide to the decimal equivilent of the percent. {ie: 0.1})')
rate = float(input('Enter percent Annual Interest Rate: '))
print(' ')

print('How many times per year is the interest compounded?')
print('[12 for monthly, 4 for quarterly, or 1 for annually]')
print('Assume 12 for debts.')
compounded = float(input('Annual Compound Frequency: '))
print(' ')

print('How many years you would like to compound your interest for?')
time = float(input('Years: '))
print(' ')

yearlyInt = invested * (rate/100)
monthlyInt = yearlyInt / 12
#Amount Saved per Month, per Year
print('Investing', invested, 'saves ', format(monthlyInt, '.2f'), 'per month; or ', format(yearlyInt, '.2f'), ' per year.')

#Base Total Saved over Duration
base = yearlyInt * time
print('Amount saved after', time, 'years is: ', format(base, '.2f'))
#Amount Saved if all monthly Savings are Reinvested
accrual = invested * (1.0 + ((rate / 100)/ compounded)) ** (compounded * time)
accrual = accrual - invested #Comment out this line for accrual to be compounded interest, but I'm removing debt so the base investment isn't something which I get back, haha.
print('Amount of compounded savings after', time, 'years (reinvesting saved monthly interest each month) is: ', format(accrual, '.2f'))
