
import serial
from time import sleep
import time

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
    
    # received_data = ser.readline()

    int_rece = []
    rece = received_data

    seconds = time.time()
    print("Seconds since epoch =", seconds) 
    print("Node ID " + str(rece[0]))
    print("Battery %" + str(rece[1]))
    print("X " + str(twos_comp(rece[2],8)))
    print("Y " + str(twos_comp(rece[3],8)))
    print("Z " + str(twos_comp(rece[4],8)))
    

            
    
