import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "stocks.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()
def add_entry(ticker,name,icon):#ticker,name company,icon url
	c.execute("INSERT INTO stocks (ticker,name,icon) VALUES (?,?,?)",
	(ticker,name,icon))
	conn.commit()
	#c.close()
	#conn.close()

def find_entry(ticker):
	c.execute('SELECT * FROM stocks WHERE ticker= (?);',(ticker,))
	info = c.fetchone()
	return info


#Example
#add_entry("AMD","Advanced Micro Devices, Inc.","https://logo.clearbit.com/amd.com")



'''



if __name__ == "__main__":
	pass
'''
