import os
import serial
import time
import pytools

class log:
    def write(data):
        dateArray = pytools.clock.getDateTime()
        string = str(dateArray[0]) + "-" + str(dateArray[1]) + "-" + str(dateArray[2])
        try:
            pytools.IO.appendFile('lsu-logs\\' + string + ".log", data)
        except:
            pytools.IO.saveFile('lsu-logs\\' + string + ".log", data)

class arduino:
    def connect():
        comNumber = -1
        while comNumber == -1:
            comNumber = 4
            if comNumber == -1:
                log.write("Connection Faliure. Device not detected.")
                time.sleep(10)
                log.write("checking again...")
        arduino.conn = serial.Serial(port='COM' + str(comNumber), baudrate=115200, timeout=.1)

    conn = False

    def write(x):
        global arduino
        arduino.write(bytes(x, 'utf-8'))

    def read(arduinon):
        data = arduinon.readline()
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
            out = arduino.read(arduino)
            try:
                if out[0] == 123:
                    print(str(out.replace(b'}\r\n', b'}'))[2:][:-1])
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
