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
import pandas_datareader.data as web
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
import datetime,math
from sklearn.neighbors import KNeighborsRegressor as knn
import matplotlib.dates as mdates
clf = LinearRegression()#n_jobs=-1)

days=240
sight=480
scaler = MinMaxScaler(feature_range=(0, 1))
start = datetime.datetime(2010, 1, 1)

end = datetime.datetime.today()+ datetime.timedelta(days=days)
dayss=(end-start).days
predicted_list=[end - datetime.timedelta(days=x) for x in range(days)]
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
clf.fit(X,y)
#plt.plot(data)
predictions=[]
for i in range(days):
    predictions.append(clf.predict([(y+predictions)[-(sight+1):-1]])[0])

dat = pd.DataFrame(y+predictions)
mavg = dat.rolling(window=50).mean()
plt.plot(date_list[sight+1:]+predicted_list,mavg)
plt.plot(date_list[sight+1:],y,color='red')
plt.plot(predicted_list,predictions,color="blue")
plt.title(stock+" Prediction")
plt.ylabel('Price')
plt.legend(("Rolling AVG","actual","predicted"))
plt.show()
