---
typora-copy-images-to: ../Figures
---

## GPIO (General-purpose input/output)

GPIO (General-purpose input/output) are hardware pins rows which locate in the top of RPi board. Raspberry Pi use GPIO pins to interact with other hardware including sensors, motors, and many many other peripheral devices.

There are actually two major GPIO naming systems: **BCM** which is often used in python language, and **wiringPi** which is often used in C language. 



To check GPIO installation:

```
gpio -v
```

```
gpio readall
```

- **GPIO** are your standard pins that simply be used to turn devices on and off. For example, a LED.
- **I2C** ([Inter-Integrated Circuit](https://en.wikipedia.org/wiki/I²C)) pins allow you to connect and talk to hardware modules that support this protocol (I2C Protocol). This will typically take up 2 pins.
- **SPI** ([Serial Peripheral Interface Bus](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)) pins can be used to connect and talk to SPI devices. Pretty much the same as I2C but makes use of a different protocol.
- **UART** ([Universal asynchronous receiver/transmitter](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver/transmitter)) are the serial pins used to communicate with other devices.
- **DNC** stands for do not connect, this is pretty self-explanatory.
- The **power pins** pull power directly from the Raspberry Pi.
- **GND** are the pins you use to ground your devices. It doesn’t matter which pin you use as they are all connected to the same line.

![gpio](/home/rshu/Documents/RaspberryPI/Figures/gpio.jpg)

