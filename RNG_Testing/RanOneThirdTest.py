import random

#Cobbled together in a mobile notepad interface while drinking my morning coffee at work.
sampleSize = int(input('Enter a sample size: '))

while sampleSize != 0:

    case1 = 0
    case2 = 0
    case3 = 0

    for i in range (0, sampleSize):

        randNum = random.randint(0,2) #need 0 AND upperbound divisible by 3, otherwise case 3 is only hit when number is EXACTLY 3
#OR the randoms are only ints and 0,2 would work

        if randNum < 1:
               case1 += 1
        elif randNum < 2:
               case2 += 1
        else:
               case3 += 1

    print ("Chose case1 ", (case1/sampleSize*100), "% of the time.", sep='')
    print ("Chose case2 ", (case2/sampleSize*100), "% of the time.", sep='')
    print ("Chose case3 ", (case3/sampleSize*100), "% of the time.", sep='')

    sampleSize = int(input('Enter a new sample size OR 0 to quit: '))
