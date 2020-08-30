import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import style

#read dataframe from csv file
df = pd.read_csv("stock_data.csv", index_col=0, parse_dates=True)

#read stock ticker from stock_ticker.txt
file_object = open('stock_ticker.txt', 'r') 
line = file_object.read() 
file_object.close()

#check that stock_ticker.txt contains valid ticker
if line == 'default':
    sys.exit("Unable to read stock data. Please run extract_data.py first")

#stock ticker
ticker = line

#create a simple moving 30-day average
SMA_short = pd.DataFrame()
SMA_short['Adj Close'] = df['Adj Close'].rolling(window=30).mean()

#create a simple moving 100-day average
SMA_long = pd.DataFrame()
SMA_long['Adj Close'] = df['Adj Close'].rolling(window=100).mean()

df['SMA Short'] = SMA_short['Adj Close']
df['SMA Long'] = SMA_long['Adj Close']

# returns array of buy and sell prices based on simple moving averages algorithm
def signals(data):
    buy = []
    sell = []

    #flag indicates wether the short term MA is currently above the long term MA
    flag = -1
    
    for i in range(len(data)):
        short = df['SMA Short'][i]
        long= df['SMA Long'][i]
        current = df['Adj Close'][i]
        
        if short > long:
            if flag != 1:
                buy.append(current)
                sell.append(np.nan)
                flag = 1
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        elif short < long:
            if flag != 0:
                buy.append(np.nan)
                sell.append(current)
                flag = 0
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    
    return (buy, sell)

buy_sell = signals(df)
df['Buy Signal Price'] = buy_sell[0]
df['Sell Signal Price'] = buy_sell[1]
print(df)

#Visualize the data

# plot styles
plt.style.use('fivethirtyeight')
plt.figure(figsize=(14,5))

plt.plot(df["Adj Close"], label=ticker, linewidth=2.0, alpha=0.6)
plt.plot(df['SMA Short'], label='SMA30', linewidth=2.0, alpha=0.4)
plt.plot(df['SMA Long'], label='SMA100', linewidth=2.0, alpha=0.4)
plt.scatter(df.index, df['Buy Signal Price'], label='Buy', marker='^', color='green')
plt.scatter(df.index, df['Sell Signal Price'], label='Sell', marker='v', color='red')
plt.title(f'{ticker} Close Price History')
plt.ylabel('Price ($USD)')
plt.legend(loc='best')
plt.show()