import sqlite3

#create a connection
connection = sqlite3.connect('sensordata.db')

# create a cursor
curs = connection.cursor() 

#update the data
curs.execute("Update sensordata set Sent = 0 where Time=1663858583.7005565")
connection.commit()
curs.close()
connection.close()

