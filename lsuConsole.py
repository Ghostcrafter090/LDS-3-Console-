import os
import serial
import time
import pytools

class log:
    def write(data):
        print(data.replace("\n", ""))
        dateArray = pytools.clock.getDateTime()
        string = str(dateArray[0]) + "-" + str(dateArray[1]) + "-" + str(dateArray[2])
        try:
            pytools.IO.appendFile('lsu-logs\\' + string + ".log", data)
        except:
            pytools.IO.saveFile('lsu-logs\\' + string + ".log", data)

class arduino:
    def connect():
        comNumber = -1
        while (comNumber < 100) and (arduino.conn == False):
            comNumber = comNumber + 1
            try:
                arduino.conn = serial.Serial(port='COM' + str(comNumber), baudrate=115200, timeout=.1)
            except:
                log.write("Connection Faliure. Device not detected.")
                time.sleep(1)
                log.write("checking again...")

    conn = False

    def write(x):
        arduino.conn.write(bytes(x, 'utf-8'))

    def read():
        data = arduino.conn.readline()
        return data

def main():
    arduino.connect()
    while True:
        try:
            # string = input("C:> ")
            # i = 0
            # while i < len(string):
            #     ard_write(string[i])
            #     time.sleep(0.0001)
            #     i = i + 1
            out = arduino.read()
            try:
                if out[0] == 123:
                    dateArray = pytools.clock.getDateTime()
                    string = str(dateArray[0]) + "-" + str(dateArray[1]) + "-" + str(dateArray[2])
                    try:
                        log.write(str(out.replace(b'}\r\n', b'}'))[2:][:-1] + "\n")
                    except:
                        log.write(str(out.replace(b'}\r\n', b'}'))[2:][:-1] + "\n")
            except:
                pass
        except:
            arduino.conn = False
            while arduino.conn == False:
                arduino.connect()
