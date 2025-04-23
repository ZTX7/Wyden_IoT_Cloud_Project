# ACOMPANHAMENTO PROJETO IOT CLOUD



Caso o Mosquitto emperre com 2 processos:

- Mapeie os processos com esse comando

  *netstat -a -n -o | findstr :1883*

- Elimine os processos com esse:

  *taskkill /PID **numero do processo** /F*

- Em outro terminal com o endereço do mosquitto para testar a mensagem do Node. 

  *mosquitto_sub -h 127.0.0.1 -t iot/nodesyrius*



### 13/04/2025

Após a configuração da comunicação entre Node e Mosquitto Broker, verifiquei que precisava configurar o mosquito para poder autorizar conexões externas.

No arquivo **"mosquitto.conf"** inseri respectivamente: 

"listener 1883"

"allow_anonymous true" 

## A resposta com base no código:

Wi-Fi conectado: ('192.168.100.106', '255.255.255.0', '192.168.100.1', '192.168.100.1')
MQTT Conectado
Mensagem MQTT enviada!


## Resposta no CMD Mosquitto: 

1744581864: New connection from 192.168.100.106:1516 on port 1883.
1744581864: New client connected from 192.168.100.106:1516 as NodeMCU (p2, c1, k0).
1744581864: No will message specified.
1744581864: Sending CONNACK to NodeMCU (0, 0)
1744581864: Received PUBLISH from NodeMCU (d0, q0, r0, m0, 'iot/nodesyrius', ... (20 bytes))

