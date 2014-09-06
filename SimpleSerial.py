import serial
class translate:
    def __init__(self):
        self.__ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=3)

    def textWrite(self, command):
        self.__ser.write(bytearray(command + " \n",'ascii')) 

    def rawWrite(self, command):
        self.__ser.write(command + " \n")
        
    def read(self):
        return self.__ser.readlines()
        
