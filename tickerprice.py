import yfinance as yf
cached_currency = {

}
currency = {
    'us_market':'$'
}
  
def given_ticker(ticker):
    
    try:info = yf.Ticker(ticker).info
    except KeyError:
        return False,["Something went wrong when getting {}!".format(ticker)]
    else:
        market_info = info['market']
        logo_url=info['logo_url']
        name = info['shortName']
        stock = yf.download(ticker,period='5m',interval='1m')
        currency_symbol = currency.get(market_info,'')
        stock_price  = round(float(stock.tail(1)['Open']),2)
        form_stock_price = currency_symbol + str(stock_price)
        return True,[form_stock_price,logo_url,name]

def get_price(ticker):
    stock = yf.download(ticker,period='5m',interval='1m')
    stock_price  = round(float(stock.tail(1)['Open']),2)
    currency_symbol = '$'
    form_stock_price = currency_symbol + str(stock_price)
    return form_stock_price
if __name__ == "__main__":
    pass




