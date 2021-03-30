import time
import adafruit_bh1750
import board
from ISStreamer.Streamer import Streamer


# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Fridglyzer"
BUCKET_NAME = "Fridglyzer"
BUCKET_KEY = "V4YRQ7HB39GL"
ACCESS_KEY = "ist_BQsWk-sOdzWzz1-aANne7TBz_GNISkfB"
MINUTES_BETWEEN_READS = 1
# ---------------------------------


# BH1750 settings
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)
sensor.resolution = 1 # LOW(3) / MID(0) / HIGH(default)(1)


# Initial State settings
streamer = Streamer(bucket_name=BUCKET_NAME,
                    bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

previousReading = 0

while True:


    # -------BH1750(Light Sensor)-----------------
    #print("%.2f Lux" % sensor.lux)
    #streamer.log("Lux", sensor.lux)
    
    # if sensor.lux > 3 
        #fridge is in use
    

    if (sensor.lux > 20 and previousReading == 0):
        previousReading = 1
        print("high prev reading", str(previousReading))
        print(sensor.lux)
        streamer.log("Lux", 1)
        streamer.flush()
    elif (sensor.lux < 20 and previousReading == 1):
        previousReading = 0
        #print(streamer.LogQueue)
        streamer.log("Lux", 0)
        print("prev reading", str(previousReading))
        print("low light", str(sensor.lux))
        streamer.flush()


    # For Testing uncomment the 5-second sleep and console prints.
    #streamer.flush()
    #time.sleep(2)

    # For Final Product uncomment use longer sleep and remove prints.
    # time.sleep(60*MINUTES_BETWEEN_READS)
