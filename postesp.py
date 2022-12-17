import requests
import sqlite3
import time

#create a connection
connection = sqlite3.connect('sensordata.db')

#url of server
url = 'http://192.168.50.50:5000/api/v1/sensors/create'

# create a cursor
curs = connection.cursor() 

while True:
    #select all rows which have not been sent
    curs.execute("SELECT * FROM sensordata WHERE sent=0")

    # copy the data into rows

    rows = curs.fetchall()

    for i in rows:
        tosend = {'Nodeid' : i[0],'Battery' : i[1], 'X' : i[2], 'Y' :i[3], 'Z' : i[4], 'Time' : i[5], 'Sent' : True }
        result = requests.post(url, json= tosend)
        if bool(result.text) == True:
            query = """UPDATE sensordata SET Sent = ? WHERE Time = ?"""
            data = (True,i[5])
            curs.execute(query,data)
            connection.commit()
            print("successfully sent data!")

    time.sleep(3)



