import random

#Cobbled together in a mobile notepad interface while drinking my morning coffee at work.

while sampleSize != 0

    case1 = 0
    case2 = 0
    case3 = 0

    for i = 0 i < sampleSize i++

        randNum = random(0,3) #need 0 AND upperbound divisible by 3, otherwise case 3 is only hit when number is EXACTLY 3
#OR the randoms are only ints and 0,2 would work

        if randNum < 1
               case1++
        elif randNum < 2
               case2++
        else
               case3++
    print (chose case1 case1/sampleSize % of the time)
    print (case2)
    print (case3)

   Input choose a new sample size
