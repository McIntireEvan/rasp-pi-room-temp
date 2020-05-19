import adafruit_dht
from board import D4
from time import sleep
from influxdb import InfluxDBClient
import datetime

dht_device = adafruit_dht.DHT22(D4)

client = InfluxDBClient('localhost', 8086, 'grafana', 'grafanapw', 'home')

while True:
    sleep(2.5)
    print("starting read")
    try:
        t = dht_device.temperature
        h = dht_device.humidity

        if t is not None and h is not None:
            f = (9.0 / 5.0) * t + 32

            print("Temp={0:0.1f}*F Hum={1:0.1f}%".format(f, h))

            time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            print(time)

            vals = [{
                "measurement": "temperature",
                "tags": {
                    "room": "bedroom"
                    },
                "time": time,
                "fields":{
                        "value": f
                    }
                }, {
                "measurement": "humidity",
                "tags": {
                    "room": "bedroom"
                    },
                "time": time,
                "fields":{
                        "value": h
                    }
                }]
            client.write_points(vals)

    except RuntimeError as error:
        print(error.args[0])
