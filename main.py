from machine import Pin, I2C
import bme280_float as bme280
import time, network, json
import request_http as rh


led = Pin(2, Pin.OUT)

def pisca(led):
    for _ in range(3):
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(0.5)


if __name__ == '__main__':
    led.value(1)

    try:
        pisca(led)

        # Inicializa o I2C e sensor BME280
        i2c = I2C(scl=Pin(5), sda=Pin(4))
        sensor = bme280.BME280(i2c=i2c)

        # Conexão Wi-Fi
        SSID = "#$MOOKE$#"
        PASSWORD = "Ragnarock1233."

        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(SSID, PASSWORD)

        while not wifi.isconnected():
            time.sleep(1)

        print("Wi-Fi conectado:", wifi.ifconfig())



        # Loop principal
        while True:
            temp, pres, umi = sensor.values
            alt = sensor.altitude

            payload = {
                'temperature': {'value': temp},
                'humidity': {'value': umi},
                'pressure': {'value': float(pres)},
                'altitude': {'value': alt}
            }

            try:
                rh.insert_update_feeds(payload, rh.HEADERS)
                pisca(led)
                print('Enviado:', json.dumps(payload))
                time.sleep(15)

            except Exception as e:
                print('Erro ao enviar:', e)

    except Exception as e:
        print('Erro principal:', e)
