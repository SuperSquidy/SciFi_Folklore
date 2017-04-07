import random
import os
import fileinput

#variables
direct = 'Text_Files'
rando = 'Generated_Files'
walkthroughs = []
texty = []
allWalkthroughs = []


#actually getting all the files
filenames = os.listdir(direct)
#print filenames

#opening, reading, and adding the files to 'walkthroughs' the files
for f in filenames:
    text_org = open(os.path.join(direct, f))
    text = text_org.read()
    text = text.split('.')
    n = 0
    for index in text:
        text[n] = text[n].replace('\n',' ')
        #stripping out every freaking type of random puctuation there could be in the least efficient way possible        
        text[n] = text[n].strip(',')
        text[n] = text[n].strip(';')
        text[n] = text[n].strip(':')
        text[n] = text[n].strip('"')
        text[n] = text[n].strip("'")
        text[n] = text[n].strip('/')
        text[n] = text[n].strip('?')
        text[n] = text[n].strip('<')
        text[n] = text[n].strip('>')
        text[n] = text[n].strip('[')
        text[n] = text[n].strip(']')
        text[n] = text[n].strip('{')
        text[n] = text[n].strip('}')
        text[n] = text[n].strip('\\')
        text[n] = text[n].strip(')')
        text[n] = text[n].strip('(')
        text[n] = text[n].strip('*')
        text[n] = text[n].strip('&')
        text[n] = text[n].strip('^')
        text[n] = text[n].strip('%')
        text[n] = text[n].strip('$')
        text[n] = text[n].strip('#')
        text[n] = text[n].strip('@')
        text[n] = text[n].strip('!')
        text[n] = text[n].strip('~')
        text[n] = text[n].strip('`')
        text[n] = text[n].strip('\=')
        text[n] = text[n].strip('\-')
        text[n] = text[n].strip('_')
        text[n] = text[n].strip('\+')
        n+=1
    walkthroughs.append(text)
    text_org.close


#flattening the list
extend = allWalkthroughs.extend
for l in walkthroughs:
    extend(l) 

#shuffling the list together
random.shuffle(allWalkthroughs) 
print ('Shuffled Walkthroughs')

#writing the file
already_there = os.listdir(rando)
#print already_there

newName = input(("Enter the new file name: "))

while newName+'.txt' in already_there:
    print ('****File already exists****')
    newName = str(input(("Enter a different file name: ")))

newWalkthrough = open(os.path.join(rando,newName+'.txt'), 'w')
s = 0
for g in allWalkthroughs:
    newWalkthrough.write(allWalkthroughs[s])
    s += 1    
newWalkthrough.close()
print ('File Saved.')



