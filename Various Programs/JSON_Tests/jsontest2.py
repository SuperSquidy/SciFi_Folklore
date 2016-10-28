import json

# a basic example of classes for subject, action, and location

sentenceText1="""
{
      "sentence": " When you are floating in the ocean, head towards the lighthouse and get inside.",
      "subject": {
        "text": "you"
      },
      "action": {
        "text": "are floating",
        "lemmatized": "be float",
        "verb": {
          "text": "float",
          "tense": "present"
        }
      },
      "location": {
        "text": "in the ocean"
      }
    }
"""


  
class Subject:
	def __init__(self):
		self.text=""
		
	def CreateFromData(self, data):
		self.text = data["text"]
			
		
class Action:
	def __init__(self):
		self.text=""
		self.lemmatized=""
		self.verbText=""
		self.verbTense=""
		
	def CreateFromData(self, data):
		self.text = data["text"]
		self.lemmatized = data["lemmatized"]
		v = data["verb"]
		self.verbText = v["text"]
		self.verbTense = v["tense"]
		
		
		
class Location:		
	def __init__(self):
		self.text=""
		
	def CreateFromData(self, data):
		self.text = data["text"]		
		  
  
    

sentence = json.loads(sentenceText1)

subject = Subject()
action = Action()
location = Location() 

subject.CreateFromData (sentence["subject"])

action.CreateFromData (sentence["action"])

location.CreateFromData (sentence["location"])

print subject.text
print action.verbText
print action.lemmatized
print location.text






