import time
import smbus2
import bme280
from ISStreamer.Streamer import Streamer


# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Fridgylzer"
BUCKET_NAME = "Fridgylzer"
BUCKET_KEY = "N8AWTRNSJEWF"
ACCESS_KEY = "ist_BQsWk-sOdzWzz1-aANne7TBz_GNISkfB"
MINUTES_BETWEEN_READS = 10
# ---------------------------------

# BME280 settings
port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params_BME280 = bme280.load_calibration_params(bus, address)


# Initial State settings
streamer = Streamer(bucket_name=BUCKET_NAME,
                    bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:

    # -------BME280(Temperature / Humidity Sensor)-------

    # Get Data from BME280 Sensor
    bme280data = bme280.sample(bus, address, calibration_params_BME280)
    humidity = format(bme280data.humidity, ".1f")
    temp_c = bme280data.temperature
    #temp_f = (temp_c * 1.8) + 32

    # Send Temp and Humidity to Web Dashboard (Initial State)
    streamer.log("Temperature(C)", temp_c)
    #streamer.log("Temperature(F)", temp_f)
    streamer.log("Humidity(%)", humidity)
    streamer.flush()





    # For Testing uncomment the 5-second sleep and console prints.
    #time.sleep(3)
    #print(temp_c, temp_f,humidity)

    # For Final Product uncomment use longer sleep and remove prints.
    time.sleep(60*MINUTES_BETWEEN_READS)
