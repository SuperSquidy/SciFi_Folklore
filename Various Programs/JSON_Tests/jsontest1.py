import json

jsontext="""
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
  
    

data = json.loads(jsontext)

print data["sentence"]
print data["location"]

action = data["action"]
verb = action["verb"]
verbTense = verb["tense"]

print action
print verb
print verbTense

