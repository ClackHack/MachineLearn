from Modelsk import Model
import pickle
english= open("data/Language/English.txt","r").read().split("\n")
spanish=open("data/Language/Spanish.txt","r").read().split("\n")
data=[]
for i in spanish:
    p = i[4:]
    pp = ""
    for j in p:
        if j == " ":
            break
        pp+=j
    data.append(pp)
