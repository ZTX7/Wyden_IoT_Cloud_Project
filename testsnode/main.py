from machine import Pin, I2C
import bme280_float as bme280
import time, urequests, ujson, network


led = Pin(2, Pin.OUT)

def pisca(led):
    for i in range(3):
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(0.5)

try:

    pisca(led)
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    sensor = bme280.BME280(i2c=i2c)

    try: 

        SSID = "#$MOOKE$#"
        PASSWORD = "Ragnarock1233."

        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(SSID, PASSWORD)

        while not wifi.isconnected():
            time.sleep(1)

        print("Wi-Fi conectado:", wifi.ifconfig())
    
    except Exception as e:
        print(f"Error: {e}")

    # Token do dispositivo no ThingsBoard
    ACCESS_TOKEN = 'NpB4Kefxg2TPKoVZrqb9' #grupo03

    # Endpoint HTTP do ThingsBoard
    url = 'https://thingsboard.cloud/api/v1/{}/telemetry'.format(ACCESS_TOKEN)
    headers = {'Content-Type': 'application/json'}

    while True:
        temp, pres, umi = sensor.values
        alt = sensor.dew_point  
 
        payload = {
            'node-data': {
                    'temperatura': temp,
                    'umidade': umi,
                    'pressao': pres, 
                    'altitude': alt,
                },
            'LinkPDF': 'https://drive.google.com/file/d/1QZUmZwVIkU8cjRNEMWY8ZiBo4mC6TEYX/view?usp=sharing'
        }

        try:
            response = urequests.post(url, headers=headers, data=ujson.dumps(payload))
            pisca(led)
            print('Enviado:', payload, '| Status:', response.status_code)
            response.close()

        except Exception as e:
            print('Erro ao enviar:', e)
            
except Exception as e:
    print(f"Error: {e}")


