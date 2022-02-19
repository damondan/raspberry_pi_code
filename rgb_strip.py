#!/usr/bin/python3
from rpi_ws281x import *
import time

num_of_secs = 6
LED_COUNT = 120
LED_PIN = 18
LED_FREQU_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 25
LED_INVERT = False
LED_CHANNEL = 0

while (True):
    # request = input("RGB --> ")
    red, blue, green = input(
        "Enter 3 RGB color numbers ... o f f to quit --> ").split()
    if (red != "o"):
        strip = Adafruit_NeoPixel(
            LED_COUNT, LED_PIN, LED_FREQU_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        for x in range(0, LED_COUNT):
            strip.setPixelColor(x, Color(int(255), int(0), int(0)))
            strip.show()
            time.sleep(.07)
            strip.setPixelColor(x, Color(int(red), int(blue), int(green)))
            strip.show()

    else:
        strip = Adafruit_NeoPixel(
            LED_COUNT, LED_PIN, LED_FREQU_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        for x in range(0, LED_COUNT):
            strip.setPixelColor(x, Color(0, 0, 0))

        strip.show()
        quit()


