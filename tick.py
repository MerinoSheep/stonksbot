import yfinance as yf


currency = {
    'us_market': '$'
}


def given_ticker(ticker):

    try:
        info = yf.Ticker(ticker).info
    except KeyError:
        return False, ["Something went wrong when getting {}!".format(ticker)]
    else:
        try:
            market_info = info['market']
        except KeyError:
            return False, ["No market information on {}!".format(ticker)]
        logo_url = info['logo_url']
        try:
            name = info['shortName']
        except KeyError:
            return False, ["{} does not have enough info!".format(ticker)]
        # If 'No data found for this date range, symbol may be delisted' increase period
        stock = yf.download(ticker, period='30m', interval='1m')
        currency_symbol = '$'
        # return info
        try:
            curr_stock_price = round(float(stock.tail(1)['Open']), 2)
        except TypeError:
                return False, ["{} is not traded enough!".format(ticker)]

        prev_stok_price = round(float(stock.head(1)['Open']), 2)
        form_stock_price = currency_symbol + str(curr_stock_price)
        # False emoji means decrease in price an True means increase on the period
        change = True if curr_stock_price > prev_stok_price else False
        return True, [form_stock_price,name, logo_url, change]


def get_price(ticker):
    stock = yf.download(ticker, period='30m', interval='1m')
    curr_stock_price = round(float(stock.tail(1)['Open']), 2)
    prev_stok_price = round(float(stock.head(1)['Open']), 2)
    currency_symbol = '$'
    form_stock_price = currency_symbol + str(curr_stock_price)
    change = True if curr_stock_price > prev_stok_price else False
    return form_stock_price, change


if __name__ == "__main__":
    pass


#print(get_price('AMD'))
