import adafruit_dht
from board import D4
from time import sleep
from influxdb import InfluxDBClient
import datetime

dht_device = adafruit_dht.DHT22(D4)

client = InfluxDBClient('localhost', 8086, 'grafana', 'grafanapw', 'home')


def make_measurement(name: str, tags, value):
    time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    print("Measured {0} as {1} at {2}".format(name, value, time))
    return {
        "measurement": name,
        "tags": tags,
        "time": time,
        "fields": {
            "value": value
        }
    }


tags = {
    "room": "bedroom"
}

while True:
    sleep(2.5)
    print("Starting read")
    measurements = []
    try:
        t = dht_device.temperature
        if t is not None:
            f = (9.0 / 5.0) * t + 32

            m_t = make_measurement("temperature", tags, f)
            measurements.append(m_t)

    except RuntimeError as error:
        print(error.args[0])
    try:
        h = dht_device.humidity
        if h is not None:
            m_h = make_measurement("humidity", tags, h)
            measurements.append(m_h)

    except RuntimeError as error:
        print(error.args[0])

    if len(measurements) > 0:
        client.write_points(measurements)
