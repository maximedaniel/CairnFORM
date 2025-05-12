#include <Adafruit_NeoPixel.h>

#define PIN         6       // Pin where NeoPixel is connected
#define NUM_LEDS    12      // Change this to match the number of LEDs in your strip

Adafruit_NeoPixel strip(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  // Light up the current LED in white
  for(int i = 0; i < NUM_LEDS; i++){
  strip.setPixelColor(i, strip.Color(50, 50, 50));
  }
  strip.show();
  delay(1000); // Wait for 1 second
  strip.clear();       // Turn off all LEDs
  strip.show();
  delay(1000); // Wait for 1 second
}
