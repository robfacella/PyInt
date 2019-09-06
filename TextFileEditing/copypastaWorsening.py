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

#print(os.path.join('Output', 'out.txt'))

inFile = open(os.path.join('Input', 'in.txt'))
print ('Opened', os.path.join('Input', 'in.txt'), ' as inFile.')

print(inFile.readlines())
