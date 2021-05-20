from Modelsk import Modelc as Model
import numpy
from PIL import Image
import pickle
import os
data=[]
key=[]
data.append([[1,1],1,0])
key.append([1,0])
'''for root, dirs, files in os.walk("Data/Faces"):
   for i in files:
      img = Image.open("Data/Faces/"+i).convert("LA").resize((400,400))
      top=img.crop((0,0,400,200))
      bottom=img.crop((0,200,400,400))
      data.append(top.getdata())
      key.append(bottom.getdata())
a = numpy.array(data)
b = numpy.array(key)
tda=a.reshape(len(a),-1)
tdb=b.reshape(len(b),-1)
print("Data Parsed")
m=Model(tda,tdb)
print("Training...")
m.train()
print("Trained")'''
m = Model(data,key)
with open("dataset/facecomp.txt","rb") as f:
   m.clf=pickle.load(f)
print("Saved")
data=[]
key=[]
i = "f.jpg"
img = Image.open("Data/Faces/"+i).convert("LA").resize((400,400))
top=img.crop((0,0,400,200))
bottom=img.crop((0,200,400,400))
data.append(top.getdata())
key.append(bottom.getdata())
a = numpy.array(data)
tda=a.reshape(len(a),-1)
x=m.predicts(tda)
'''
x1=numpy.array(x)
aa=x1.reshape(400,400)

'''
pic=[]
for i in range(len(x[0])):
    if i % 400==0:
        
        pic.append(x[i:i+399])
        
aa = numpy.array(pic)
img=Image.fromarray(aa)
img.show()
