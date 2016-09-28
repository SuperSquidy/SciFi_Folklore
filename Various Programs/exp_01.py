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



import numpy as np
np.random.seed(0)

#sigmoid curve used for probability
# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)