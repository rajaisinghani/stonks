import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()
#default
ticker = 'TSLA'
df = web.DataReader("TSLA", 'yahoo', start, end)
#df.reset_index(inplace=True)
#df.set_index('Date')
print(df.head())


