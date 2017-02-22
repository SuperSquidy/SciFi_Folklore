import json
import os

direct = 'TestJSONs'

class Subject():
    def __init__(self):
#        self.name = word
        self.text = 'testing'
        self.pov = ''
        self.plurality = ''
        self.freq = ''
        
    def __main__(self,word):
        Subject.name = word
        

#need to figure out how i'm going to have the data structured.    
    def getInfo(self,data):
        self.text = data["text"]
        
class Action:
    	def __init__(self):
         self.text = ""
         self.lemmatized = ""
         self.verbText = ""
         self.verbTense = ""


def parse_json(raw):
#    files = []
#    jsons = []

#if wanna make dictionaries
#    Subjects = {text:[], entities:[], keywords:[]}
#    Actions = {text:[], tense:[]} #more things
#    Objects = {text:[], keywords:[]}
#    Locations = {text:[]}

    #actually getting all the files
    filenames = os.listdir(raw)
    
    
    #opening, and parsing the json files and putting them into lists/format that we can actually use
    for f in filenames:
        json_org = open(os.path.join(raw, f))
        jos = json.load(json_org)
        jos_r = jos["relations"]
        n = 0
        for index in jos_r:
            dictSub = {}
            info = jos_r[n]

            #sentence as a whole
            textSentence = info["sentence"]
            
            #subject of the sentence
            #subject[text:<text>,entities:[{type:<category>,text:<text>}],keywords:[{text:<text>}]]
            subject = info["subject"]
            textSubject = subject["text"]
            textSubject = Subject()
            dictSub[textSubject] = textSubject
            print(dictSub[textSubject])
            #textSubject = Subject(subject["text"])
            print(textSubject.text)
        n+=1
        
        
parse_json(direct)

subject = Subject()
print(subject)










