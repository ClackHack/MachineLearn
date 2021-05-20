from Modelsk import Modeli as Model
from PIL import Image
import os
import numpy, pickle
data=[]
key=[]
'''
for root, dirs, files in os.walk("Data/celebs/Tom"):
   for i in files:
      img = Image.open("Data/celebs/Tom/"+i)
      nimg=img.resize((400,400))
      data.append(nimg.getdata())
      key.append(0)

for root, dirs, files in os.walk("Data/celebs/Jenny"):
   for i in files:
      img = Image.open("Data/celebs/Jenny/"+i)
      nimg=img.resize((400,400))
      data.append(nimg.getdata())
      key.append(1)
a = numpy.array(data)
size=len(a)
tda = a.reshape(size,-1)
t=tda
'''
okey={0:"Tom",1:"Jennifer"}
tda=[]
key=[]

m = Model(tda,key)
#m.setOutputKey(okey)
#m.train()
with open("dataset/celebpic.txt","rb") as f:
    m.clf = pickle.load(f)
    
data=[]
key=[1,1,1,0,0]
for root, dirs, files in os.walk("Data/celebs/Test"):
   for i in files:
      img = Image.open("Data/celebs/Test/"+i)
      nimg=img.resize((400,400))
      data.append(nimg.getdata())
a = numpy.array(data)
size=len(a)
tda = a.reshape(size,-1)
p = m.predicts(tda)
print(p)
print(m.measure(p,key))
