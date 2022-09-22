import serial
from time import sleep
import time

import sqlite3

# create a connection
connection = sqlite3.connect('sensordata.db')

# create a cursor
curs = connection.cursor()

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is



ser = serial.Serial ("/dev/ttyAMA0", 115200)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)

    int_rece = []
    rece = received_data

    seconds = time.time()
    
    #create a entry into the sensordata table
    intID = rece[0]
    intBattery = rece[1]
    intX = twos_comp(rece[2],8) 
    intY = twos_comp(rece[3],8)
    intZ = twos_comp(rece[4],8)
    dbTime = seconds
    sent = False;
    
    print("Seconds since epoch =", dbTime) 
    print("Node ID " + str(intID))
    print("Battery %" + str(intBattery))
    print("X " + str(intX))
    print("Y " + str(intY))
    print("Z " + str(intZ))

    #dump data into table
    curs.execute("INSERT INTO sensordata (Nodeid, Battery, X, Y, Z, Time, Sent) VALUES(?, ?, ?, ?, ?, ?, ?)", (intID,
    intBattery, intX,
    intY, intZ, dbTime, sent))

    # save changes and exit
    connection.commit()
    
    
curs.close()
connection.close()
            
    
