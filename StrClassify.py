from Modelsk import Model
import pickle
with open("dataset/Word.txt","rb") as f:
    data,targets=pickle.load(f)
for i in range(len(data)):
    data[i] = data[i].replace("-","").replace(" ","").replace("'","")
    
m = Model(data,targets,)
m.train()
m.setOutputKey({0:"Positive",1:"Negative"})
