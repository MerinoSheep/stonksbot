import tick
import sql_db
import csv
import time
import sqlite3
import os.path
from dotenv import load_dotenv
from iexfinance.stocks import Stock
from iexfinance import utils
load_dotenv()
IEX_TOKEN = os.getenv('IEX_TOKEN')

def write():
    with open('NYSE.txt') as csv_f:
        csv_reader = csv.reader(csv_f,delimiter='\t')
        for row in csv_reader:
            ticker = row[0]
            if(sql_db.find_entry(ticker) != None):
                print("{} already has a database entry".format(ticker))
            else:
                try:
                    found,stock_info = tick.given_ticker(row[0])#[form_stock_price,logo_url,name]
                except IndexError:
                    print("cant process row") 
                if(found):
                        print("{} added".format(ticker))
                        sql_db.add_entry(ticker,stock_info[2],stock_info[1])
                        #time.sleep(2)
                else:
                    print(stock_info) # A not found stock will return an error string while a found stock returns a tuple
def update_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "stocks.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c2 = conn.cursor()
    c.execute('SELECT * FROM stocks') 
    for row in c:
        ticker = row[0]
        if(row[1]==None or row[1] == 'Null' ): #shortname update
            try:
                name = tick.get_short_name(ticker)             
            except KeyError:
                pass
            else:
                c.execute("UPDATE stocks set name = ? where ticker = ?", (name,ticker))
                print("update name")
        if(row[3]==None or row[3] == 'Null' ): #exchange update       
            stock_IEX = Stock(ticker, tocken = IEX_TOKEN)           
            try:
                exchange = stock_IEX.get_company()['exchange']
            except utils.exceptions.IEXQueryError:
                print("Could not complete action")
            else:
                c2.execute("UPDATE stocks set exchange = ? where ticker = ?", (exchange,ticker))
                print("Added {} for {}".format(exchange,ticker))
                conn.commit()
          
    c.close()
    c2.close()
    conn.close()

update_db()

# write()