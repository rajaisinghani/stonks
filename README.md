# stonks
Algorithmic trading bot in Python bot that sends buy and sell signals to users based on simple moving average algorithm

1. Install required dependencies
```
$ pip install pandas
$ pip install numpy
$ pip install matplotlib
$ pip install pandas_datareader
```

2. Extract historical stock price data
```
$ python extract_data <stock_ticker> <time_period>
```
``<stock_ticker>`` enter stock symbol or ticker symbol of stock (for example AAPL for Apple or TSLA for Tesla)
``<time_period>`` indicate the length of historical data <br />
valid time periods include
  * 6m - 6 months
  * 1y - 1 year
  * 5y - 5 years
  * 10y - 10 years

The following script below extracts historical price data of Apple stock from the last 5 years 
```
$ python extract_data AAPL 5y
```
output below

![Historical price data for APPL](/img/price_chart.png)

3. Finish later
```
$ python algo_trade
```

