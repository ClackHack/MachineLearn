from sklearn import tree

names = open("nameslist.txt","r").read().split("\n\n")

boys = []
for i in range(1,len(names),3):
    boys.append(names[i])
girls = []
for i in range(2,len(names),3):
    girls.append(names[i])
place = [[],[]]
for i in range(len(boys)):
    place[0].append(boys[i])
    place[1].append(girls[i])
'''import pickle
boys.append("Clay")
girls.append("Cleo")
with open("Listnames.txt","wb") as f:
    pickle.dump([boys,girls],f)
assert 0

'''
import pickle
with open("Listnames.txt","rb") as f:
    names = pickle.load(f)
boys = names[0]
girls = names[1]

Y = [0 for i in boys]
for i in girls:
    Y.append(1)
x=[]
for i in boys:
    x.append(i)
for i in girls:
    x.append(i)
    
alpha={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
       'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
       'k': 11, 'l': 12, 'm': 13,'n': 14, 'o': 15,
       'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
       'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
       'z': 26}
X=[]
#x=["Dave","Emma","Clay"]

for i in range(len(x)):
    
    place = []
    for j in x[i]:
        
        place.append(alpha[j.lower()])
    num = 11 - len(place)
    for i in range(num):
        place.append(0)
    X.append(place)

while 1:        
    y = [0,1,0,1]
    clf = tree.DecisionTreeClassifier()
    clf=clf.fit(X,Y)
    name = input("Name: ")
    if name=="":
        break
    place=[]
    for i in name:
        place.append(alpha[i.lower()])
    num = 11-len(place)
    for i in range(num):
        place.append(0)
    result = {0:"Boy",1:"Girl"}
    t = clf.predict([place]).tolist()[0]
    print(result[t])
    
