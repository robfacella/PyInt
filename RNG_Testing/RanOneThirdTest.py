import random
import time

#Starting Sample Size
sampleSize = int(input('Enter a sample size: '))
while sampleSize != 0: #runs until user enters 0
    start_time = time.time()
    case = [0, 0, 0]
    for i in range (0, sampleSize): #Runs from 0 to sampleSize-1 (Therefore sampleSize Times)
        randNum = random.randint(0,2) #Chooses random integer {0, 1, or 2}
        if randNum < 1:
               case[0] += 1 #if zero counter
        elif randNum < 2:
               case[1] += 1 #if one counter
        else:
               case[2] += 1 #if two counter
    for j in range (0, len(case)): #iterate over list and print how often each case was hit.
        print ("Chose case ", (j + 1), " ", (case[j]/sampleSize*100), "% of the time.", sep='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print(' ')
    sampleSize = int(input('Enter a new sample size OR 0 to quit: ')) #Run again or exit with 0
