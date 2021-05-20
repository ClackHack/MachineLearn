from PIL import Image
from Modelsk import Modeli as Model
loc=["Dogs/"+str(i)+".jpg" for i in range(1,9)]
loc+=["Cats/"+str(i)+".jpg" for i in range(1,9)]
import numpy
data = []
for i in loc:
    img = Image.open("data/"+i)
    nimg=img.resize((400,400))
    data.append(nimg.getdata())
a = numpy.array(data)
size=len(a)
tda = a.reshape(size,-1)
t=tda
key=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
okey={0:"Dog",1:"Cat"}
m = Model(tda,key)
m.setOutputKey(okey)
m.train()
test = ["Dogs/"+str(i)+".jpg" for i in range(11,21)]
#test += ["Cats/"+str(i)+".jpg" for i in range(9,11)]
data = []
for i in test:
    img = Image.open("data/"+i)
    nimg=img.resize((400,400))
    #nimg.show()
    data.append(nimg.getdata())
a = numpy.array(data)
size=len(a)

tda = a.reshape(size,-1)
    
key=[0,0,1,1]
okey={0:"Apple",1:"Orange"}
for i in tda:
    print(m.predict(i))
def meval(p,t):
    if len(p) != len(t):
        raise ValueError
    total = len(p)
    count=0
    for i in range(len(p)):
        if p[i] == t[i]:
            count+=1
    return total / count
#print(meval(m.predicts(tda),key)*100,"%")