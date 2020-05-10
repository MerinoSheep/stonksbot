import pandas as pd
import yfinance as yf
import numpy as np
df = pd.read_json('generic.json')
def given_name(name):
    
    print(df.loc[df['Ticker']=='B'])
  
def given_ticker(ticker):
    stock=yf.download(ticker,period='1m',interval='1m')
    #return stock.squeeze().tail(1)['High']
    return round(float(stock.squeeze().tail(1)['High']),2)


if __name__ == "__main__":
    pass


#print(given_ticker('AAPL'))