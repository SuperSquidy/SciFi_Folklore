#take the json information and read it, and split the information to read the 'sentence' part in 'relations'
#there are multiple 'sentence' objects, so how call them for each individually
#would look at 'relations[n]' and access the information the same way as in jsontest1.py within that

#Types of things in the json files:
#   not all are included in every section of the list
#subject[text:<text>,entities:[{type:<category>,text:<text>}],keywords:[{text:<text>}]] 
#action[text:<text>,lemmatized:<root>,verb[text:<text>,tense:<tense>]]
#object[text:<text>,keywords:[{text:<text>}],sentiment:{type:<category>,score:<number>}]--i don't care about sentiment
#location[text:<prepositionalphrase>]
#temporal[text:<text>,decoded:{type:<category>,value:<numbers i don't understand>}]

import json
import os

direct = 'Walkthrough_Alchemy'


class Subject:
    def __init__(self):
        self.text = ''
        self.pov = ''
        self.plurality = ''
        self.count = 1
        self.probability = 0

#need to figure out how i'm going to have the data structured.    
    def getInfo(self,data):
        #subject of the sentence
        #subject[text:<text>,entities:[{type:<category>,text:<text>}],keywords:[{text:<text>}]]
        subject = data["subject"]
        self.text = subject["text"]

    def POV(self):
        if(self.text == 'I' or self.text == 'we' or self.text == 'We'):
            self.pov = 'first-person'
        elif (self.text == 'you' or self.text == 'You' or self.text == "y'all" or self.text == "Y'all"):
            self.pov = 'second-person'
        elif (self.text == ''):
            print("***No valid subject found***")
        else:
            self.pov = 'third-person'

        
class Action:
        def __init__(self):
         self.text = ""
         self.lemmatized = ""
         self.verbText = ""
         self.verbTense = ""




Subjects = {}
    
def parse_json(raw):
#    files = []
#    jsons = []

#if wanna make dictionaries
    #Subjects = {"text":[], entities:[], keywords:[]}
    #Actions = {text:[], tense:[]} #more things
    #Objects = {text:[], keywords:[]}
    #Locations = {text:[]}



    #actually getting all the files
    filenames = os.listdir(raw)
    
        
    #opening, and parsing the json files and putting them into lists/format that we can actually use
    for f in filenames:
        json_org = open(os.path.join(raw, f))
        jos = json.load(json_org)
        jos_r = jos["relations"]
        n = 0
        for index in jos_r:
            info = jos_r[n]

            #sentence as a whole
            textSentence = info["sentence"]
            #print textSentence 
            
            #subject of the sentence
            #subject[text:<text>,entities:[{type:<category>,text:<text>}],keywords:[{text:<text>}]]
            subject = info["subject"]
            textSubject = subject["text"]
            
            #print "subject", subject
            
            #the different things that could possibly be in the under 'subject'
            if "entities" in subject:
                entities = subject["entities"]
                e = 0
                for l in entities:
                    entity = entities[e]
                    textEntity = entity["text"]
                    categoryEntity = entity["type"]
                    e+=1
                #print "entities:" , entities
            
            if "keywords" in subject:
                keywordsSub = subject["keywords"]
                k = 0
                for l in keywordsSub:
                    keyS = keywordsSub[k]
                    textKeyword_subject = keyS["text"]
                    k+=1
               # print "keywords", keywordsSub
                
            newSubject = Subject ()
            newSubject.text = textSubject
            
            if textSubject in Subjects:
            	Subjects[textSubject].count +=1 
            else:
	            Subjects[textSubject] = newSubject
            
            
            #action of the sentence
            #action[text:<text>,lemmatized:<root>,verb[text:<text>,tense:<tense>]]
            action = info["action"]
            textAction = action["text"]
            rootAction = action["lemmatized"]
            verb = action["verb"]
            textVerb = verb["text"]
            verbTense = verb["tense"]

            #all the rest are things that may or maynot be included in a sentence
            
            #object[text:<text>,keywords:[{text:<text>}],sentiment:{type:<category>,score:<number>}]--not using sentiment
            if "object" in info:
                obj = info["object"]
                textObject = obj["text"]
                if "keywords" in obj:
                    keywordsObj = obj["keywords"]
                    k = 0
                    for l in keywordsObj:
                        keyO = keywordsObj[k]
                        textKeyword_object = keyO["text"]
                        k+=1
            
            #location[text:<prepositionalphrase>]
            if "location" in info:
                location = info["location"]
                textLocation = location["text"]
            
            #temporal[text:<text>,decoded:{type:<category>,value:<numbers i don't understand>}]--not using decoded
            if "temporal" in info:
                temporal = info["temporal"]
                textTemp = temporal["text"]
            n+=1

parse_json(direct)
  
  
# figure out probabilities 

# first, how many subjects are there?

numSubjects = float(len(Subjects))
  
for k in Subjects.keys():
	Subjects[k].probability = Subjects[k].count / numSubjects 

	print k + ";" + str(Subjects[k].probability)
	