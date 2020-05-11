import pandas as pd
import yfinance as yf
import numpy as np
currency={
    'us_market':'$'
}
df = pd.read_json('generic.json')
def given_name(name):
    
    print(df.loc[df['Ticker']=='B'])
  
def given_ticker(ticker):
    market_info = yf.Ticker(ticker).info['market']
    stock = yf.download(ticker,period='1m',interval='1m')
    currency_symbol = currency.get(market_info,'')
    stock_price  = round(float(stock.tail(1)['Open']),2)
    #return market_info
    return currency_symbol + str(stock_price)
   

if __name__ == "__main__":
    pass

#print(given_ticker('AMD'))
