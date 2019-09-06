import os

#Windows && Unix FileSystem Support
#Read each line of a file
#split line to strings
#CharByChar : Substring
#### Randomly capitalize/lowercase letters
#### Random 1337-speak
#Reassemble and Output to a New Output file
#os.chdir('..') #bash-like, this DOES work
#print (os.getcwd()) #get Current Working Dir



inFile = open(os.path.join('Input', 'in.txt'))
print ('Opened', os.path.join('Input', 'in.txt'), ' as inFile.txt')

#print(inFile.readlines()) #Print List of all Lines in the File. \n as line separator.
#print(inFile.readlines()) #Need to close and ReOpen to read again. Or move Read Pointer in another way.

outFile = open(os.path.join('Output', 'out.txt'), 'w')
print('Opened', os.path.join('Output', 'out.txt'), ' as outFile.txt for writing')

lines = inFile.readlines()

#To copy in.txt to out.txt
#Should open outFile for 'w'rite for the first line, and then 'a'ppend the rest of the lines.
#Or do separate writes just work provided the writer doesn't close and reopen... #<- Yes, this one.
for line in lines:
    outFile.write(line)
print('Copied', os.path.join('Input', 'in.txt'), 'to', os.path.join('Output', 'out.txt'),'!!')
inFile.close()
outFile.close()
print('Closed inFile and outFile')
