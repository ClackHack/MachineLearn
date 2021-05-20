import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier as MLP
#import pandas_datareader.data as web
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
import datetime,math
from sklearn.neighbors import KNeighborsRegressor as knn
import matplotlib.dates as mdates
from sklearn.neural_network import MLPRegressor
clf=MLPRegressor()#knn(n_neighbors=13)#MLPRegressor()# LinearRegression()#,knn(n_neighbors=2)]#,MLPRegressor()]   

#days=3
sight=10
scaler = StandardScaler()
#start = datetime.datetime(2010, 1, 1)

#end = datetime.datetime.today()+ datetime.timedelta(days=days)
#dayss=(end-start).days
#predicted_list=[end - datetime.timedelta(days=x) for x in range(days)]
#predicted_list.reverse()

#stock=input("Stock: ").upper()
#df = web.DataReader(stock, 'yahoo', start, end)
data = open("roobet.txt","r").read().split(",")
data = [float(i) for i in data]
X,y=[],[]
#fig, ax = plt.subplots()
#formatter = mdates.DateFormatter("%Y")
#date_list=list(data.reset_index()["Date"])
for i in range(0,len(data)-(sight+1)):
    X.append([j for j in data[i:i+sight]])
    y.append(data[i+sight+1])
#fig, axs = plt.subplots(3)
#fig.suptitle("Roobet Prediction")
#colors=["Blue","Green","Purple"]
#plts = axs
#print(X,y)
#pltt.plot(range(len(y)),y,color='red')
#X=scaler.fit_transform(X)
clf.fit(X,y)
print("Model Fitted")
#plt.plot(data)
    

    #dat = pd.DataFrame(y+predictions)
    #mavg = dat.rolling(window=3).mean()
    #pltt.plot(range(len(mavg)),mavg)
    #pltt.plot(range(len(predictions)),predictions,color=color)
    #pltt.legend(("actual","Rolling Avg.","Prediction"))
predictions=input(f"Last {sight+3}: ").split(",")
predictions = [float(i) for i in predictions]
print(len(predictions))
while 1:
    
    #s=scaler.transform([(predictions)[-(sight+1):-1]])
    print("Predicted: ",clf.predict([(predictions)[-(sight+1):-1]]))
    x=input("Actual: ")
    if x=="": break    
    predictions.append(float(x))
#plt.title(stock+" Prediction")
#plt.ylabel('Price')
#plt.xlabel("Index")
#plt.legend(("actual","Rolling Avg.","LinearReg","KNN"))


