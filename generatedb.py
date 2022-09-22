import sqlite3

connection = sqlite3.connect('sensordata.db')
curs = connection.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS sensordata (Nodeid INT, Battery INT, X INT, Y INT, Z INT, Time DOUBLE, Sent BOOLEAN)''')

connection.commit()
connection.close()


