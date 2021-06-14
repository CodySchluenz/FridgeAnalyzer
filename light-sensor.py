import adafruit_bh1750
import board
from ISStreamer.Streamer import Streamer


# --------- User Settings ---------
BUCKET_NAME = "INSERT BUCKET NAME HERE"
BUCKET_KEY = "INSERT BUCKET KEY HERE"
ACCESS_KEY = "INSERT ACCESS KEY HERE"
MINUTES_BETWEEN_READS = 1
# ---------------------------------


# BH1750 settings
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)
sensor.resolution = 1


# Initial State settings
streamer = Streamer(bucket_name=BUCKET_NAME,
                    bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

previousReading = 0

while True:

    if (sensor.lux > 5 and previousReading == 0):
        previousReading = 1
        print("high prev reading", str(previousReading))
        print(sensor.lux)
        streamer.log("Lux", 1)
        streamer.flush()
    elif (sensor.lux < 5 and previousReading == 1):
        previousReading = 0
        streamer.log("Lux", 0)
        print("prev reading", str(previousReading))
        print("low light", str(sensor.lux))
        streamer.flush()
