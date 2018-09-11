#include <Adafruit_NeoPixel.h>
#include <stdio.h>
#include <stdlib.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif
#define NUMPIXELS        6
#define EIR_NB           1
#define EIR_0            6

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
Adafruit_NeoPixel pixels [EIR_NB] = {Adafruit_NeoPixel(NUMPIXELS, EIR_0, NEO_GRB + NEO_KHZ800)};

int SIZE_PACKAGE = 4;

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.



int delayval = 500; // delay for half a second

void setup() {
  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
  Serial.begin(9600);
#if defined (__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  // End of trinket special code

  for(int j=0;j<EIR_NB;j++){
      pixels[j].begin(); // This initializes the NeoPixel library.
  }
}

void loop() { 
  // Read serial input:
   char package[SIZE_PACKAGE];
  while (Serial.available() > SIZE_PACKAGE - 1) {
    Serial.readBytes(package, SIZE_PACKAGE);
    if(package[0] >= 0 && package[0]<EIR_NB){
      for(int i = 0; i < NUMPIXELS; i++){
        pixels[package[0]].setPixelColor(i, pixels[package[0]].Color(package[1], package[2], package[3]));
      }
      pixels[package[0]].show(); 
    }
  }
}

