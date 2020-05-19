# rasp-pi-room-monitor

Room Temperature and Humidity Monitoring dashboard in Grafana.

This README outlines what I did to set it all up, but is by no means a definitive guide.

## Parts Needed
- Raspberry Pi (Any version should work, this runs fine on a Raspberry Pi 1 Revision 2) running latest Raspbian
- USB Wifi Adapter if the Pi doesn't support WiFi
- DHT22 Sensor
- 10k Ohm resistor (should come with the sensor)
- 1 Male/Male jumper wire
- 3 Male/Female jumper wires

## Setting up the sensor

See wiring in https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

## Installing Libraries

Make sure python3 and pip3 are installed and up to date. You'll also need the following:

```
pip3 install adafruit-circuitpython-dht
pip3 install influxdb
sudo apt-get install libgpiod2
```

## Installing Influx, Grafana
See https://simonhearne.com/2020/pi-influx-grafana/

Only changes: Installing Grafana as directed in that blog didn't work for me. I installed from https://grafana.com/grafana/download?platform=arm and it worked fine.

## Running the script
Get the python script in this repo, replace influx details if you changed them, and run it.

Go to Grafana, make a new dashboard, and copy the model I have, or make your own.

# TODO
- Add Barometric pressure sensor; possibly replace DHT22 with BME280. Need to do more research
- Add air quality/co2 like https://www.adafruit.com/product/3566
- cleanup script
- explore using a cheaper network-enabled board that "phones home" to a central pi that commits to the db and runs grafana.
