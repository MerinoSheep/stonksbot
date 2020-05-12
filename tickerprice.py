import yfinance as yf
cached_currency = {

}
currency = {
    'us_market':'$'
}
  
def given_ticker(ticker):
    
    try:info = yf.Ticker(ticker).info
    except KeyError:
        return False,"Something went wrong when getting {}!".format(ticker)
    else:
        market_info = info['market']
        logo_url=info['logo_url']
        stock = yf.download(ticker,period='5m',interval='1m')
        currency_symbol = currency.get(market_info,'')
        stock_price  = round(float(stock.tail(1)['Open']),2)
        #return info
        return True,[currency_symbol + str(stock_price),logo_url]

   

if __name__ == "__main__":
    pass

print(given_ticker('AMD'))


