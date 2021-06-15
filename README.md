# Fridge Analyzer

<img src="https://www.eatgreaterdesmoines.org/wp-content/themes/EatGreaterDesMoines/images/logo-color-small.png" width="150" align="right">

**Insert some form of mission statement here and/or the purpose of this thing here**


### Warning

**Insert some warning about how this is a prototype here and is subject to change**


## Materials

Required Materials:

| Item  | Quantity | Price |
| ------------- | ------------- | ------------- |
| [BH1750 Light Sensor - STEMMA QT / Qwiic](https://www.adafruit.com/product/4681)   | 1 | $4.50 |
| [BME280 I2C Temperature Humidity Sensor - STEMMA QT](https://www.adafruit.com/product/2652)   | 1 | $14.95 |
| [STEMMA QT / Qwiic JST SH 4-Pin Cable - 200mm Long](https://www.adafruit.com/product/4401)   | 2 | $0.95 |
| [SparkFun Qwiic or Stemma QT SHIM for Raspberry Pi / SBC](https://www.adafruit.com/product/4463)   | 1 | $1.50 |
| [5V 2.5A Switching Power Supply with 20AWG MicroUSB Cable](https://www.adafruit.com/product/1995)   | 1 | $7.50 |
| [Pi Foundation Raspberry Pi Zero Case + Mini Camera Cable](https://www.adafruit.com/product/3446)   | 1 | $5.95 |
| [Raspberry Pi Zero WH (Zero W with Headers)](https://www.adafruit.com/product/3708)   | 1 | $14.00 |
| [16GB Card with NOOBS 3.1 for Raspberry Pi Computers](https://www.adafruit.com/product/4266)   | 1 | $14.95 |


<br/>
Optional Materials:

| Item  | Quantity | Price |
| ------------- | ------------- | ------------- |
| [Small Plastic Project Enclosure - Weatherproof with Clear Top](https://www.adafruit.com/product/903)   | 1 | $9.95 |
| [Hook-up Wire Spool Set - 22AWG Solid Core - 6 x 25 ft](https://www.adafruit.com/product/1311)   | 1 | $15.95 |
| [USB OTG Host Cable - MicroB OTG male to A female](https://www.adafruit.com/product/1099)   | 1 | $2.50 |
| [USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply](https://www.adafruit.com/product/961)   | 1 | $27.50 |
| [Flanged Weatherproof Enclosure With PG-7 Cable Glands](https://www.adafruit.com/product/3931)   | 1 | $9.95 |
| [Silicone Sealant 100% RTV - 2.8 oz Squeeze Tube -Clear-](https://www.amazon.com/gp/product/B0063U2RWU/ref=ox_sc_act_title_1?smid=AZ3IOW8ZC7Q2O&psc=1)   | 1 | $6.42 |
| [Command Strips](https://smile.amazon.com/Command-Water-Resistant-Refill-Strips-4-Strip/dp/B000WSNM9Q)   | 1 | $6.49 |
| [Micro SD to USB card reader](https://www.amazon.com/dp/B006T9B6R2?psc=1&ref=ppx_yo2_dt_b_product_details)   | 1 | $15.99 |

## <br/>Hardware Setup
`pip install cfn-lint`. If pip is not available, run
`python setup.py clean --all` then `python setup.py install`.

## Software Setup

### Raspberry Pi Initial Setup

The microSD comes pre-installed with the full Raspberry Pi OS, so all that is left to do is configure it. After the Raspberry Pi boots up, follow the on screen prompts to configure your language, timezone, wifi, and software updates. The software updates will take around 30 minutes to complete and it is very important that the Raspberry Pi does not lose power during this time.
<br>
<img src="img\initial-setup.png">

### Raspberry Pi Configuration - SSH
In order to access the Raspberry Pi remotely from another computer or device, you will need to enable SSH.

1. Launch `Raspberry Pi Configuration` from the `Preferences` menu
2. Navigate to the `Interfaces` tab
3. Select `Enabled` next to `SSH`
4. Click `OK`

<img src="img\ssh.jpg">

### Raspberry Pi Configuration - I2C
I2C is a very commonly used standard designed to allow one chip to talk to another. So, since the Raspberry Pi can talk I2C we can connect it to a variety of I2C capable chips and modules. The sensors we use rely on I2C, so we have to enable it.

1. Launch `Raspberry Pi Configuration` from the `Preferences` menu
2. Navigate to the `Interfaces` tab
3. Select `Enabled` next to `I2C`
4. Click `OK`

<img src="img\i2c.png">

### Install Python Libraries

### Python Code

### Run on startup / reboot

## Initial State Setup

### Create Dashboard

### Alerting Setup

### Watchdog Setup



`brew install cfn-lint`

### Docker

In `cfn-python-lint` source tree:

```shell
docker build --tag cfn-python-lint:latest .
```

