#input--new information
#hidden_layer--essentially the network's memory
#output--what the program 'decides' the next thing will be based on the input and hidden

#so basically, what I want to do overall is have a reccurent function which is
#built to take the new input, 'add' it to the hidden layer, use the hidden layer
#to help determine the output

#want to teach the network a bunch of information and have it be able to predict the next word
#when you give it a noun.
#i.e. you give it the input 'you' and it decides the next most likely verb/word to come after

#in terms of a weighted matrix, the hidden layer will act as the reference for
#decision of the most likely next word, and the hidden layer will change with each iteration
#based on the LTSM logic 



#make a array of sentence with an array of word and in the word have an array of letters
#then either:
#Add up the array to use for predictions--con: order wouldn't matter
#OR
#use a hash funtion to keep the order of things--con: would get really big really fast--hash is one way
#OR
#use ascii ord()--to number, chr()--to letter
#then use bin to convert to binary, trim off the Ob, then converto to list and append to an array

#use Alchemy to create a dictionary of nouns, verbs, etc in the text as a basis for the program to start building off of to identify what the parts of speech are.

import random
import os
import fileinput
import numpy as np
np.random.seed(0)

direct = 'Test_Texts'
walkthroughs = []
texty = []
allWalkthroughs = []

#sigmoid curve used for probability
# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)

def split_to_sent(raw):
    texts = []
    sentences = []

    #actually getting all the files
    filenames = os.listdir(raw)
    #print filenames
    
    #opening, reading, and adding the files to 'walkthroughs' the files
    for f in filenames:
        text_org = open(os.path.join(raw, f))
        text = text_org.read()
        text = text.split('.')
        n = 0
        for index in text:
            text[n] = text[n].replace('\n','')
            n+=1
        texts.append(text)
        text_org.close
    
    extend = sentences.extend
    for l in texts:
        extend(l)
    
    return(sentences)

def split_to_words(sent):
    words = []
    n = 0
    for f in sent:
        interim_words = []
        interim_words = sent[n].split()
#        print(sent[n])
        i = 0
        for w in interim_words:
            words.append(interim_words[i])
#            print(interim_words[i])
            i+=1
#            print(words)
        n+=1
    return words
    
#if want to have all letters in same list
def split_to_lettersA(words):
    letters = []
    n = 0
    for f in words:
        letters.extend(words[n])
        n+=1
    return(letters)
    
#if want to keep words separated in nested lists
#preferred    
def split_to_lettersB(words):
    letters = []
    n = 0
    for f in words:
        interim_lets = []
        lets = []
        interim_lets = words[n]
        i = 0
        for l in interim_lets:
            lets.append(interim_lets[i])
            i+=1
        letters.append(lets)
        n+=1
    return(letters)

#use if using split_to_lettersA    
def make_letters_asciiA(letters):
    binary = []
        
    return(binary)

#use if using split_to_lettersB
def make_letters_asciiB(letters):
    numberletters = []
    n = 0
#   convert to ascii
    for l in letters:
        asci = []
        interim_asci = []
        interim_asci = letters[n]
        i = 0
        for a in interim_asci:
            coded = ord(interim_asci[i])
            asci.append(coded)
            i+=1
        numberletters.append(asci)
        n+=1        
    return(numberletters)

#use with other B variants
def make_ascii_biB(asci):
    binary = []
    n = 0
    for a in asci:
        bi = []
        interim_bi = []
        interim_bi = asci[n]
        i = 0
        for b in interim_bi:
            numbs = bin(interim_bi[i])
            numbs2 = numbs[2:]
            bi.append(numbs2)
            i+=1
        binary.append(bi)
        n+=1
    return(binary)

#to be used after matrix stuff
def make_bi_asciiB(bi):
    asci = []
    n = 0
    for a in bi:
        asc = []
        interim_asc = []
        interim_asc = bi[n]
        i = 0
        for b in interim_asc:
            numbs = int(interim_asc[i],2)
            asc.append(numbs)
            i+=1
        asci.append(asc)
        n+=1
    return(asci)

def make_ascii_lettersB(asc):
    numberletters = []
    n = 0
#   convert to ascii
    for l in asc:
        asci = []
        interim_asci = []
        interim_asci = asc[n]
        i = 0
        for a in interim_asci:
            coded = chr(interim_asci[i])
            asci.append(coded)
            i+=1
        numberletters.append(asci)
        n+=1        
    return(numberletters)

def make_letters_wordsB(lets):
    words = []
    n = 0
    for l in lets:
        word = []
        interim_word = []
        interim_word = lets[n]
#       somehow flatten the list into a string
    
doingThings = split_to_sent(direct)
print(doingThings)
doingThings_2 = split_to_words(doingThings)
#print(doingThings_2)
doingThings3A = split_to_lettersA(doingThings_2)
#print(doingThings3A)
doingThings3B = split_to_lettersB(doingThings_2)
#print(doingThings3B)
doingThings4B = make_letters_asciiB(doingThings3B)
#print(doingThings4B)
doingThings5B = make_ascii_biB(doingThings4B)
print(doingThings5B)
doingThings6B = make_bi_asciiB(doingThings5B)
#print(doingThings6B)
doingThings7B = make_ascii_lettersB(doingThings6B)
print(doingThings7B)
