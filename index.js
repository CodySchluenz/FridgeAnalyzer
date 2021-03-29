// # --------- Imports ---------
var IS = require("initial-state");
const BME280 = require("bme280-sensor");
var bh=require("BH1750")
// # ---------------------------------

// # --------- Initial State User Settings ---------
SENSOR_LOCATION_NAME = "Fridgylzer";
BUCKET_NAME = "Fridgylzer";
BUCKET_KEY = "BBK3MJ765C8G";
ACCESS_KEY = "ist_BQsWk-sOdzWzz1-aANne7TBz_GNISkfB";
MINUTES_BETWEEN_READS = 5;
// # ---------------------------------

// setup data bucket
var bucket = IS.bucket(BUCKET_KEY, ACCESS_KEY);

// Push event to initial state
bucket.push("Demo State", "active");

setTimeout(function () {
  // Push another event
  bucket.push("Demo State", "inactive");
}, 1000);
console.log("hi");

const options = {
  i2cBusNo: 1, // defaults to 1
  i2cAddress: BME280.BME280_DEFAULT_I2C_ADDRESS(), // defaults to 0x77
};
const bme280 = new BME280(options);
// Read BME280 sensor data, repeat
//
//var bh=require("BH1750").connect(i2c, addr)
//bh.start(resolution,onetime)
const readSensorData = () => {
  bme280
    .readSensorData()
    .then((data) => {
      // temperature_C, pressure_hPa, and humidity are returned by default.
      // I'll also calculate some unit conversions for display purposes.
      //
      data.temperature_F = BME280.convertCelciusToFahrenheit(
        data.temperature_C
      );
      data.pressure_inHg = BME280.convertHectopascalToInchesOfMercury(
        data.pressure_hPa
      );
      bucket.push("temperature_C", data.temperature_C);
      bucket.push("temperature_F", data.temperature_F);
      bucket.push("pressure_hPa", data.pressure_hPa);
      bucket.push("pressure_inHg", data.pressure_inHg);

      console.log(`data = ${JSON.stringify(data, null, 2)}`);
      setTimeout(readSensorData, 2000);
    })
    .catch((err) => {
      console.log(`BME280 read error: ${err}`);
      setTimeout(readSensorData, 2000);
    });
};

// Initialize the BME280 sensor
//
bme280
  .init()
  .then(() => {
    console.log("BME280 initialization succeeded");
    readSensorData();
  })
  .catch((err) => console.error(`BME280 initialization failed: ${err} `));
