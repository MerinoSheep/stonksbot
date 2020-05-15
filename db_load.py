import tick
import sql_stock
import csv
import time
def write():
    with open('NYSE.txt') as csv_f:
        csv_reader = csv.reader(csv_f,delimiter='\t')
        for row in csv_reader:
            ticker = row[0]
            if(sql_stock.find_entry(ticker) != None):
                print("{} already has a database entry".format(ticker))

            else:
                try:
                    found,stock_info = tick.given_ticker(row[0])#[form_stock_price,logo_url,name]
                except IndexError:
                    print("cant process row") 
                if(found):
                        print("{} added".format(ticker))
                        sql_stock.add_entry(ticker,stock_info[2],stock_info[1])
                        #time.sleep(2)
                else:
                    print(stock_info) # A not found stock will return an error string while a found stock returns a tuple

write()