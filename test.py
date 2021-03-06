import serial

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
line = []


while True:
    for c in ser.read():
        ser.write("A")
        line.append(c)
        if c == '\n':
            print("Line: " + ''.join(line))
            line = []
            break

ser.close()
