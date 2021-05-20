from sklearn import tree
import abc
import pickle
class Model (object):
    def __init__(self,data,key,strdata=True,limit=13):
        self.data=data
        self.clf=tree.DecisionTreeClassifier()
        self.wdata=[]
        self.key=key
        self.limit=limit
        self.alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
       'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
       'k': 11, 'l': 12, 'm': 13,'n': 14, 'o': 15,
       'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
       'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
       'z': 26}
        if strdata:
            self.data=self.listtodata(data,overwrite=False)
    def strtodata(self,s,lower=True,overwrite=False):
        place=[]
        if lower: s=s.lower()
        for i in s:
            place.append(self.alpha[i])
        num = self.limit-len(place)
        for i in range(num):
            place.append(0)
        self.wdata=place
        if overwrite:
            self.data=place
        else:
            return place
    def listtodata(self,l,lower=True,overwrite=True):
        place2=[]
        
        for i in range(len(l)):
            place = []
            for j in l[i]:
                place.append(self.alpha[j.lower()])
            num = self.limit - len(place)
            for i in range(num):
                place.append(0)
            place2.append(place)
        if overwrite:
            self.data=place2
        else:
            return place2
    def train(self):
        self.clf = self.clf.fit(self.data,self.key)
    def predict(self,data,isString=True,key=False):
        if isString:
            data=self.strtodata(data)
        if key:
            return key[self.clf.predict([data]).tolist()[0]]
        return self.clf.predict([data]).tolist()[0]
        
