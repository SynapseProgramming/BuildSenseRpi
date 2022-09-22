import sqlite3

#create a connection
connection = sqlite3.connect('sensordata.db')

# create a cursor
curs = connection.cursor() 

#select all rows which have not been sent
curs.execute("SELECT * FROM sensordata WHERE sent=0")

# copy the data into rows
rows = curs.fetchall()

for i in rows:
    print(i)




