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

def split_to_letters(words):
    letters = []
    n = 0
    for f in words:
        letters.extend(words[n])
        n+=1
    return(letters)
    
def make_words_binary(word):
    binary = []    
    return(binary)
    
doingThings = split_to_sent(direct)
print(doingThings)
doingThings_2 = split_to_words(doingThings)
print(doingThings_2)
doingThings3 = split_to_letters(doingThings_2)
print(doingThings3)