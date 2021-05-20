import requests as rp
import pickle
from bs4 import BeautifulSoup as soup
import os
output="dataset/"+"foods"+".txt"
os.makedirs(os.path.dirname(output), exist_ok=True)
def save(data,key):
    with open(output,"wb") as f:
        pickle.dump([data,key],f)
url="https://www.halfyourplate.ca/fruits-and-veggies/fruits-a-z/"
page=rp.get(url)
s=soup(page.content,"html.parser")
x=s.find("div",class_="left-column").find_all("li")
a=[]
for i in x:
    place=i.text.strip()
    if " " in place or "-" in place or "*" in place:
        pass
    else:
        a.append(place)

url="https://www.halfyourplate.ca/fruits-and-veggies/veggies-a-z/"
page=rp.get(url)
s=soup(page.content,"html.parser")
x=s.find("div",class_="left-column").find_all("li")
b=[]
for i in x:
    place=i.text.strip()
    if " " in place or "-" in place or "*" in place:
        pass
    else:
        b.append(place)
c="""Bacon
Ham
Hot dogs
Jamon
Prosciutto
Salami
Sausages
Beef
Lamb
Mutton
Chicken
Turkey
Venison
Duck
Rabbit""".split('\n')
target=[]
for i in a:
    target.append(0)
for i in b:
    target.append(1)
for i in c:
    target.append(2)
data = a+b+c
save(data,target)
