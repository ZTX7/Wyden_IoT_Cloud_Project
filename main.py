import network, time, ujson
from umqtt.simple import MQTTClient
from machine import Pin, unique_id


SSID = "#$MOOKE$#"
PASSWORD = "Ragnarock1233."

led = Pin(2, Pin.OUT)

def msg():

    chip_id = hex(int.from_bytes(unique_id(), "little"))

    grupo = {
        "membros": ["Sinezio", 
                    "Felipe", 
                    "Paulo", 
                    "Bruno", 
                    "Salazar"],
        "chip_id": chip_id,
    }

    mensagem = ujson.dumps(grupo)
    return mensagem

def pisca(led):
    for i in range(3):
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(0.5)

try:

    BROKER = "mqtt.engenharias.tech"
    PORTA = 1883
    TOPICO = "iot/nodesyrius"
    CLIENT_ID = "NodeMCU"

    mqtt = MQTTClient(CLIENT_ID, BROKER, PORTA)

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    while not wifi.isconnected():
        time.sleep(1)

    print("Wi-Fi conectado:", wifi.ifconfig())

    mqtt.connect()
    print("MQTT Conectado")

    mqtt.publish(TOPICO, msg())
    pisca(led)
    print("Mensagem MQTT enviada!")

except Exception as e:
    print("Ocorreu um erro ao conectar: ", e)


