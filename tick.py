import yfinance as yf


currency = {
    'us_market': '$'
}


def given_ticker(ticker):

    try:
        info = get_info(ticker)
    except KeyError:
        return False, ["Something went wrong when getting {}!".format(ticker)]
    else:
        logo_url = info['logo_url']
        name = get_short_name(ticker)
        # If 'No data found for this date range, symbol may be delisted' increase period
        stock = yf.download(ticker, period='30m', interval='1m')
        currency_symbol = '$'
        try:
            curr_stock_price = float(stock.tail(1)['Open'])
        except TypeError:
                return False, ["{} is not traded enough!".format(ticker)]

        prev_stok_price = float(stock.head(1)['Open'])
        form_stock_price = currency_symbol + "{:0.2f}".format(curr_stock_price)
        # False emoji means decrease in price an True means increase on the period
        change = True if curr_stock_price > prev_stok_price else False
        return True, [form_stock_price,name, logo_url, change]


def get_price(ticker):
    stock = yf.download(ticker, period='30m', interval='1m')
    curr_stock_price =float(stock.tail(1)['Open'])
    prev_stok_price = float(stock.head(1)['Open'])
    currency_symbol = '$'
    form_stock_price = currency_symbol + "{:0.2f}".format(curr_stock_price)
    change = True if curr_stock_price > prev_stok_price else False
    return form_stock_price, change


def get_info(ticker):
    return yf.Ticker(ticker).info

def get_short_name(ticker):
    try:
        return get_info(ticker)['shortName']
    except KeyError:
        return False, ["{} does not have enough info!".format(ticker)]

if __name__ == "__main__":
    pass

#print( get_info('AMD'))
#print(get_price('AMD'))
