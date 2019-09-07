import os
import random
#Windows && Unix FileSystem Support
#Read each line of a file
#split line to strings
#CharByChar : Substring
##Remove Special Char {'\n' and others}
#### Randomly capitalize/lowercase letters
#### Random 1337-speak
##Add Special Char(s) back in.
#Reassemble and Output to a New Output file
def charManip(word):
    #x = 0
    newWord = '' #could/should just modify word as a substring
    for charmander in word:
        if charmander.isalpha() :
            r = random.randint(1, 2)    #Randomly changes the case of all Alphabetical char in the word string
            if r == 1 :
                charmander = charmander.upper()
            else:
                charmander = charmander.lower()
        newWord += charmander #reassembles string as newWord
        #x += 1  #print(x, 'characters in', word) #Counts "\n" as one char
    return newWord #return newWord
def wordsFromLine(line):
    wordList = line.split(" ")
    #print(wordList)
    return wordList #Takes a line of text and splits words on spaces.
#os.chdir('..') #bash-like, this DOES work
#print (os.getcwd()) #get Current Working Dir
inFile = open(os.path.join('Input', 'in.txt'))
print ('Opened', os.path.join('Input', 'in.txt'), ' as inFile.txt')
#print(inFile.readlines()) #Print List of all Lines in the File. \n as line separator.
#print(inFile.readlines()) #Need to close and ReOpen to read again. Or move Read Pointer in another way.

outFile = open(os.path.join('Output', 'out.txt'), 'w')
print('Opened', os.path.join('Output', 'out.txt'), ' as outFile.txt for writing')

lines = inFile.readlines()
#print(lines)

#To copy in.txt to out.txt
####Should open outFile for 'w'rite for the first line, and then 'a'ppend the rest of the lines.
#Or do separate writes just work provided the writer doesn't close and reopen... #<- Yes, this one.
for line in lines:
    newLine = ''
    for word in wordsFromLine(line):
        word = charManip(word)
        newLine += ' '
        newLine += word
    outFile.write(newLine)

print('Copied the modified', os.path.join('Input', 'in.txt'), 'to', os.path.join('Output', 'out.txt'),'!!')
inFile.close()
outFile.close()
print('Closed inFile and outFile')
