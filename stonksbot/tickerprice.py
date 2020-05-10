import pandas as pd
import yfinance as yf
import numpy as np
df = pd.read_json('generic.json')
def given_name(name):
    
    print(df.loc[df['Ticker']=='B'])
  
def given_ticker(ticker):
    stock=yf.download(ticker,period='1m',interval='1m')

    return round(float(stock.tail(1)['Open']),2)
   

if __name__ == "__main__":
    pass


