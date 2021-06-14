import time
import smbus2
import bme280
from ISStreamer.Streamer import Streamer


# --------- User Settings ---------
BUCKET_NAME = "INSERT BUCKET NAME HERE"
BUCKET_KEY = "INSERT BUCKET KEY HERE"
ACCESS_KEY = "INSERT ACCESS KEY HERE"
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

    # Send Temp and Humidity to Web Dashboard (Initial State)
    streamer.log("Temperature(C)", temp_c)
    streamer.log("Humidity(%)", humidity)
    streamer.flush()

    time.sleep(60*MINUTES_BETWEEN_READS)
