from Modelsk import *
import numpy as np
import requests as rp
import json
from Chatbot import speech
x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
   's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '-', '.', ',', "'", '?', '/', '0', '1', '2',
   '3', '4', '5', '6', '7', '8', '9', '!']
with open("data/conv.txt","r") as f:
    j=json.load(f)

data=[]
key=[]
for r in j:
    test=r["dialog"]
    for i in range(1,len(test)):
        
        if test[i-1]["sender_class"]=="Bot" and test[i]['sender_class']=='Human':
            place=""
            d=test[i-1]["text"]
            for v in d:
                if v in x:
                    place+=v
            data.append(place)
            place=""
            k=test[i]["text"]
            for v in k:
                if v in x:
                    place+=v
            key.append(place)
        #print(test[i]["text"],end=" - ")
        #print(test[i]["sender_class"])
    
m = ModelTalk(data,key)
#m.train()
del data
del key
del j
import pickle
m.train()

f.close()
c=0
while 1:        
    name = input("Say: ")
    if name=="":
        break
    n=m.predict(name).strip()
    print(n)
    speech.say(c,n)
    c+=1
try:
    import shutil
    shutil.rmtree('sounds',ignore_errors=True)
    
        
        
except Exception as e:
    print(e)
    print(e.with_traceback())
    pass
import os
try:
    os.mkdir("sounds")
except Exception as e:
    print(e)
    pass
