# Installation

- run `sudo apt-get update`
- run `sudo pip install adafruit-circuitpython-motorkit`
- run `sudo raspi-config` and enable I2C
- run `sudo pip install -r ./requirements.txt`

![alt text](https://github.com/maximedaniel/CairnFORM/blob/master/img/institutions.png "Logo Institutions")

## Remote Programming using a RaspberryPi configured as a WiFi AP@192.165.5.1

- connect your computer to Wi-Fi with SSID `CairnFORM` / pwd 'ESTIA64210'
- open `VNC viewer` on Windows 
- connect to `192.168.5.1` using user "pi"/ pwd "ESTIA64210"

# Changing SSID password

- sudo nano /etc/hostapd/hostapd.conf
- change password with at least 8 characters
- sudo systemctl restart hostapd

# CairnFORM

Inspired by _cairns_, CairnFORM is a shape-changing cylindrical display that simultaneously inform users at 360° using color-changing and shape-changing abilities. CairnFORM is built as a stack of expandable illuminated rings. As a use case, we use CairnFORM for visualizing and announcing variations of local renewable energy production. We deployed CairnFORM in the middle of an open plan for helping employees to shift laptop battery charge to peak hours of local renewable energy production (i.e. promoting energy cleanliness).

![alt text](https://github.com/maximedaniel/CairnFORM/blob/master/img/teaser.png "Logo Institutions")

# Designing an Expandable Illuminated Ring

The CAD model of the expandable illuminated ring is available on [OnShape](https://cad.onshape.com/documents/7d4ecae370a1e03250f148cc/w/40919688efd268263900abc1/e/6c37dd97791037a37d7dd39b). The mechanical parts and the electronic components are illustrated below. The column makes the ring stackable. A TRINAMIC stepper motor QSH4218-41-10-035 with a transmission gear activates a wheel gear. The wheel activates four pinion gears. Each pinion gear activates an axial rack and a diagonal rack. At the edge of each rack, there is an arc representing one eighth of a ring. When the ring is fully retracted, the arcs form an initial ring of ø35 cm. When the ring is fully expanded, the arcs form a ring-like shape of ø62 cm. A micro-switch sense when the ring is fully retracted. The ring is illuminated by 24 NeoPixel Digital RGB LEDs (three LEDs glued on each arc) splitted in four strips using a LED strip splitter. Each strip is soldered to flat ribbon cables, themselves glued to racks. The column is manufactured in PLA material using 3D printing. All other parts are made in translucent PMMA material using 2D laser cutting and assembled using acetone. The remaining parts, mainly support parts, are made in plywood using 2D laser cutting. Bolts, nuts, washers and glue are used to assemble all the parts together. 

![alt text](https://github.com/maximedaniel/CairnFORM/blob/master/img/specs1.jpg "Specifications Expandable Illuminated Ring")

# Hardware and software for a Stack of 10 Expandable Illuminated Rings

The hardware and software for controlling a 10-ring CairnFORM are illustrated below. CairnFORM is controlled by a Raspberry Pi 3. To control the expansion of the rings, this Raspberry Pi 3 communicates with 5 Adafruit stepper motor HATs, via an I2C bus. Each HAT controls two stepper motors (i.e., two rings). To sense when a ring is closed, the Raspberry Pi 3 communicates, via GPIO, with an Adafruit perma-proto HAT with 10 pull-up resistors (one pull-up resistor per micro-switch, i.e., per ring). To control the LEDs, the Raspberry Pi 3 communicates, via USB serial port, with an Arduino Mega 2560 with 10 PWM outputs (one PWM output per LED strip
splitter, i.e., per ring).  The hardware described allows controlling from 1 to 10 rings but more rings could be stacked by adding extra HATs and Arduino. However, the wiring harness width will allow up to ∼24 rings. 

![alt text](https://github.com/maximedaniel/CairnFORM/blob/master/img/specs2.png "Specifications Stack Expandable Illuminated Rings")

The CairnFORM driver, written in Python language (version 2.7), runs on the Raspberry Pi 3 and controls the rings in sequence or in parallel. The driver is composed of four Python classes. To set the next morphing of the stack, a CairnFormHandler class uses an array of 10 RingHandler objects. The RingHandler class models a ring (e.g., address, position, and color) and uses two queues to store
the next morphing of the ring: a queue for shape-changing and a queue for light-changing. The CairnFormHandler class calls the rings to morph in sequence or in parallel: when a RingHandler object is called to morph, it instantiates a thread in which a MotionHandler object and a LightHandler object are called for the unqueued values. Given the address of the ring, the MotionHandler object reads the associated micro-switch using the GPIO Python Library and controls the associated stepper motor using Adafruit Python Library. Given
the address of the ring, the LightHandler object sends the address and the associated RGB values to the Arduino Mega 2560 using Arduino Python Library. A C program, uploaded on the Arduino Mega card, receives the address and the RGB values from the serial port and updates the corresponding LEDs.
