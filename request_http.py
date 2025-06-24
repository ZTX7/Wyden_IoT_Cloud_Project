import urequests as requests
import json, time

ADAFRUIT_IO_USERNAME = "nome do usuario"
ADAFRUIT_IO_KEY      = "chave do adafruit"

NAME_GROUP_FEEDS = 'nome do grupo dee feeds'
DASHBOARD_NAME = "nome do dashboard"

HEADERS = {
    "X-AIO-Key": ADAFRUIT_IO_KEY,
    "Content-Type": "application/json"
}

FEEDS = ['temperature', 'humidity', 'pressure', 'altitude']

#Fiz algumas fuções para configurar o adafruit, estão funcionais, mas o nodemcu não tem recursos suficientes para executar.
def get_groups(HEADERS):
    try:
        response = requests.get(f"https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/groups", headers=HEADERS)
        print(response.status_code)
        print(response.text)
        response.close()
    except Exception as e:
        print("Erro:", e)


def create_group(HEADERS):
    response = requests.post(
        f"https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/groups",
        headers=HEADERS,
        data=json.dumps({"name": NAME_GROUP_FEEDS})
    )
    state = "error" in response.text
    response.close()
    return state, response


def create_feeds(HEADERS):
    for feed_name in FEEDS:
        response = requests.post(
            f"https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/groups/{NAME_GROUP_FEEDS.lower()}/feeds",
            headers=HEADERS,
            data=json.dumps({"name": feed_name})
        )
        state = "error" in response.text
        print(response.status_code, response.text)
        response.close()
    return state, response


def create_dashboard(HEADERS):
    response = requests.post(
        f"https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/dashboards",
        headers=HEADERS,
        data=json.dumps({"name": DASHBOARD_NAME})
    )
    state = "error" in response.text
    response.close()
    return state, response


def insert_update_feeds(data, HEADERS):
    try:
        for item in data:
            feed_url = f'https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}/groups/{NAME_GROUP_FEEDS.lower()}/feeds/{item.lower()}/data'
            payload_data = data[item]
            print(f"Enviando para {feed_url} o payload: {payload_data}")

            response = requests.post(feed_url, headers=HEADERS, data=json.dumps(payload_data))
            print(f"Status {item}: {response.status_code}, Resposta: {response.text}")
            response.close()
            time.sleep(1)

    except Exception as e:
        print("Erro:", e)


#Tentei criar uma função para criar os blocos na área do Dashboard, mas por algum motívo não consegui conectar aos feeds.
'''def formated_blocks(feed_name, NAME_GROUP_FEEDS):
        
    feed_icons = {
        'temperature': 'thermometer',
        'humidity': 'humidity',
        'pressure': 'barometer',
        'altitude': 'compass' 
    }    

    icon_to_use = feed_icons.get(feed_name.lower(), 'gauge') 
    
    block = {
                "name": feed_name.title(),
                "visual_type": "gauge",
                "column": 1,
                "row": 1,
                "size_x": 4,
                "size_y": 4,
                "properties": {
                    "showIcon": 'true',
                    "icon": icon_to_use,
                    "label": "\u00baC",
                    "minValue": "0",
                    "maxValue": "100",
                    "ringWidth": "25",
                    "minWarning": "15",
                    "maxWarning": "35",
                    "decimalPlaces": "2"
                },

                "block_feeds": [{
                        "feed": feed_name.lower(),                          
                        "group": NAME_GROUP_FEEDS.lower()
                }]
                
            }
    return block


def create_blocks(HEADERS, feed_list):
    for feed in feed_list:
        block_payload = formated_blocks(feed, NAME_GROUP_FEEDS)
        response = requests.post(f"https://io.adafruit.com/api/v2/{ADAFRUIT_IO_USERNAME}//dashboards/{DASHBOARD_NAME.lower()}/blocks", 
                                headers=HEADERS, data=json.dumps(block_payload))
        print(response.status_code)
        print(response.text)
        response.close()
    return response.json()
'''


