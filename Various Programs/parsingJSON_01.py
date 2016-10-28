import json
import os

direct = 'Walkthrough_Alchemy'


def parse_json(raw):
    files = []
    jsons = []

    #actually getting all the files
    filenames = os.listdir(raw)
    
    
    #opening, reading, and adding the files to 'walkthroughs' the files
    for f in filenames:
        json_org = open(os.path.join(raw, f))
        jos = json.load(json_org)
        jos_r = jos["relations"]
        n = 0
        for index in jos_r:
            info = jos_r[n]
            sentence = info["sentence"]
            print(sentence)
            subject = info["subject"]
            print(subject)
            n+=1

parse_json("Walkthrough_Alchemy")
 
#take the json information and read it, and split the information to read the 'sentence' part in 'relations'
#there are multiple 'sentence' objects, so how call them for each individually
#would look at 'relations[n]' and access the information the same way as in jsontest1.py within that