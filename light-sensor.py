import time
import adafruit_bh1750
import board
from ISStreamer.Streamer import Streamer


# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Fridgylzer"
BUCKET_NAME = "Fridgylzer"
BUCKET_KEY = "N8AWTRNSJEWF"
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

while True:


    # -------BH1750(Light Sensor)-----------------
    #print("%.2f Lux" % sensor.lux)
    streamer.log("Lux", sensor.lux)
    
    # if sensor.lux > 3 
        #fridge is in use
 


    # For Testing uncomment the 5-second sleep and console prints.
    streamer.flush()
    time.sleep(1)

    # For Final Product uncomment use longer sleep and remove prints.
    # time.sleep(60*MINUTES_BETWEEN_READS)
