import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import sys 

# total arguments 
n = len(sys.argv) 
if n != 3:
    sys.exit('invalid arguments')

# plot styles
plt.style.use('fivethirtyeight')
plt.figure(figsize=(14,5))

# time now
end = dt.datetime.now()

#default
ticker = 'TSLA'
df = None

#check time period input is valid
#valid time periods include 6 months(6m), 1 year(1y), 5 years(5y), 10 years(10y)
timePeriod = sys.argv[2]

if timePeriod == '6m':
    start = end - dt.timedelta(days=183)
elif timePeriod == '1y':
    start = end - dt.timedelta(days=1*365)
elif timePeriod == '5y':
    start = end - dt.timedelta(days=5*365)
elif timePeriod == '10y':
    start = end - dt.timedelta(days=10*365)
else:
    sys.exit("Invalid time period. please enter a valid time period")

#retrieve historical stock price data of given stock ticker

#read stock ticker from input
while df is None:
    #try to pull historical price data
    try:
        ticker = sys.argv[1]
        df = web.DataReader(ticker, 'yahoo', start, end)
    #error
    except:
        sys.exit("ticker is invalid. please enter a valid ticker")

# visualize historical price data as graph

plt.plot(df["Adj Close"], label=ticker, linewidth=2.0)
plt.title(f'{ticker} Close Price History')
plt.ylabel('Price ($USD)')
plt.legend(loc='best')
plt.show()

#write historical price data to csv file
print(df)
df.to_csv(r'./stock_data.csv')

#write stock ticker to txt file
file_object = open('stock_ticker.txt', 'w') 
file_object.write(f'{ticker}') 
file_object.close()

