import sqlite3

# create a connection
connection = sqlite3.connect('sensordata.db')

# create a cursor
curs = connection.cursor()

#create a entry into the sensordata table
intID = 69
intBattery = 6969
intX = 1
intY = 2
intZ = 3
dbTime = 43.345656545
sent = True

#dump data into table
curs.execute("INSERT INTO sensordata (Nodeid, Battery, X, Y, Z, Time, Sent) VALUES(?, ?, ?, ?, ?, ?, ?)", (intID, intBattery, intX,
intY, intZ, dbTime, sent))

# save changes and exit
connection.commit()
curs.close()
connection.close()




