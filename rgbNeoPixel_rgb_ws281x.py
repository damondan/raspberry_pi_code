from rpi_ws281x import *
LED_COUNT = 50
LED_PIN = 18
LED_FREQU_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 150
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQU_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()

for x in range(0, LED_COUNT):
    strip.setPixelColor(x, Color(0,255,0))

strip.show()

except KeyboardInterrupt:
    print("Keyboard Interrupt")
