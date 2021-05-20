from Modelsk import Model
import pickle
english= open("data/Language/English.txt","r").read().split("\n")
spanish=open("data/Language/Spanish.txt","r").read().split("\n")
data=[]
key=[]
for i in english:
    data.append(i)
    key.append(0)
for i in spanish:
    data.append(i)
    key.append(1)

outkey={0:'English',1:"Spanish"}
m = Model(data,key)
m.setOutputKey(outkey)
with open("models/language.txt","rb") as f:
    m.clf = pickle.load(f)
