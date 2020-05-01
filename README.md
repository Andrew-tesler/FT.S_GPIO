# FT.S_GPIO
## Introduction

![](https://img.shields.io/github/last-commit/Andrew-tesler/FT.S_GPIO?style=for-the-badge)


Please follow Readme.pdf document for overall system description. [README](https://github.com/Andrew-tesler/FT.S_GPIO/blob/master/README.pdf)



### About This Repository
This repository is for Tensor FT.S_GPIO Add On Tel board, It contains Software, Hardware and example use cases for the board.
The following document will emphasize on building and using the repository, with some examples for the product.

### Importing And Building

1. Install mbed CLI following this guide

https://os.mbed.com/docs/mbed-os/v5.15/tools/manual-installation.html

2. Install STM32CubeProgrammer following this guide

https://www.st.com/en/development-tools/stm32cubeprog.html

3. Clone the repository
```
    git clone https://github.com/Andrew-tesler/FT.S_GPIO.git
```

4. Update the repo to the latest mbed os version
```
    mbed update
```

5. compile
```
    mbed compile -m NUCLEO_F429ZI -t GCC_ARM
```

6. Using STM32Cube flash the program (windows) 'Add Linux'



### Python examples

``` Python
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
```
