import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier as MLP
import argparse
import pandas_datareader.data as web
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
import datetime,math
from sklearn.neighbors import KNeighborsRegressor as knn
import matplotlib.dates as mdates
clf = LinearRegression()#n_jobs=-1)
#clf= knn()

days=240
sight=600
scaler = MinMaxScaler(feature_range=(0, 1))
start = datetime.datetime(2005, 1, 1)

end = datetime.datetime.today()- datetime.timedelta(days=days+1)
dayss=(end-start).days
count = 0
predicted_list=[]
while len(predicted_list) != 241:
    count+=1
    if count in [0,1]:
        continue
    
    predicted_list.append(end - datetime.timedelta(days=count))
predicted_list.reverse()

stock=input("Stock: ").upper()
df = web.DataReader(stock, 'yahoo', start, end)
data = df['Adj Close']
X,y=[],[]
fig, ax = plt.subplots()
formatter = mdates.DateFormatter("%Y")
date_list=list(data.reset_index()["Date"])
for i in range(0,len(data)-(sight+1)):
    X.append([j for j in data[i:i+sight]])
    y.append(data[i+sight+1])
split=len(y)-240
X_train=X[:split]
y_train=y[:split]
clf.fit(X_train,y_train)

#plt.plot(data)
predictions=[y_train[-1]]
for i in range(days):
    predictions.append(clf.predict([(y_train+predictions)[-(sight+1):-1]])[0])

plt.plot(date_list[sight+1:],y,color='red')
plt.plot(date_list[-1*(days+1):],predictions,color="blue")
plt.title=stock+" Prediction"
plt.ylabel('Price')
plt.legend(("actual","predicted"))
plt.show()

