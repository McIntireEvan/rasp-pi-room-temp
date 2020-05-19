# rasp-pi-room-temp

## Parts Needed
- Raspberry Pi (Any version should work, this runs fine on a Raspberry Pi 1 Revision 2) running latest Raspbian
- USB Wifi Adapter if the Pi doesn't support WiFi
- DHT22 Sensor
- 10k Ohm resistor (should come with the sensor)
- 1 Male/Male jumper wire
- 3 Male/Female jumper wires

## Setting up the sensor

See wiring for https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

## Installing Libraries

Make sure python3 and pip3 are installed and up to date

Might not need the second command here? idk
```
pip3 install adafruit-circuitpython-dht
pip3 install RPI.GPIO
pip3 install influxdb
sudo apt-get install libgpiod2
```

## Installing Influx, Grafana
See https://simonhearne.com/2020/pi-influx-grafana/

Only changes: Installing Grafana as directed in that blog didn't work for me. I installed from https://grafana.com/grafana/download?platform=arm and it worked fine.

## Running the script
Get the python script in this repo, replace w/ influx details

run it, and go to grafana. make a chart and you should be able to select temperature or humidity

todo: document this more

# TODO
- Add Barometric pressure sensor; possibly replace DHT22 with BME280. Need to do more research
- Add air quality/co2 like https://www.adafruit.com/product/3566
- cleanup script
- explore using a cheaper network-enabled board that "phones home" to a central pi that commits to the db and runs grafana.
