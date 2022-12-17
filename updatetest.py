import sqlite3

#create a connection
connection = sqlite3.connect('sensordata.db')

# create a cursor
curs = connection.cursor() 

# query
query = """UPDATE sensordata SET Sent = ? WHERE Time = ?"""
data = (True,1671266688.4679153)
curs.execute(query,data)


 
connection.commit()
curs.close()
connection.close()

