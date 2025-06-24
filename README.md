# Projeto IoT - Leitura de Sensor BME280 com ESP8266 e Envio para Adafruit IO

Este projeto utiliza um microcontrolador ESP8266 para ler dados de temperatura, umidade, pressão e altitude a partir de um sensor BME280. As leituras são enviadas periodicamente para a plataforma **Adafruit IO**, permitindo a visualização remota dos dados em dashboards.

## 🛠 Tecnologias e Bibliotecas

- **MicroPython**
- **Sensor BME280 (I2C)**
- **ESP8266 (NodeMCU)**
- **Adafruit IO (API HTTP)**
- Bibliotecas:
  - `urequests` (para HTTP)
  - `network` (Wi-Fi)
  - `machine` (GPIO e I2C)

## 📁 Estrutura dos Arquivos

```
├── main.py               # Script principal: leitura dos dados e envio para a nuvem
├── bme280_float.py       # Driver do sensor BME280 para MicroPython
├── request_http.py       # Funções para interação com a API da Adafruit IO
```

## 🚀 Funcionamento

1. O ESP8266 conecta-se a uma rede Wi-Fi.
2. Inicializa o sensor BME280 via I2C.
3. Faz leituras de:
   - Temperatura
   - Pressão atmosférica
   - Umidade
   - Altitude (calculada com base na pressão e nível do mar)
4. Envia os dados para os respectivos feeds configurados na plataforma **Adafruit IO**.
5. O LED embutido no ESP8266 pisca indicando o sucesso no envio dos dados.

## 🔧 Configuração

### 1. Credenciais Wi-Fi
No arquivo `main.py`, altere as variáveis:

```python
SSID = "Seu_SSID"
PASSWORD = "Sua_Senha"
```

### 2. Configuração da Adafruit IO
No arquivo `request_http.py`, substitua:

```python
ADAFRUIT_IO_USERNAME = "seu_usuario"
ADAFRUIT_IO_KEY = "sua_chave_de_api"
NAME_GROUP_FEEDS = "nome_do_grupo"
DASHBOARD_NAME = "nome_do_dashboard"
```

### 3. Feeds Esperados
O projeto envia dados para os seguintes feeds no grupo:

- `temperature`
- `humidity`
- `pressure`
- `altitude`

> **Importante:** Crie esses feeds manualmente no grupo no Adafruit IO ou utilize as funções `create_group()` e `create_feeds()` presentes no arquivo `request_http.py`. Contudo, devido às limitações de memória do NodeMCU, essas funções podem não funcionar diretamente no microcontrolador.

## 🏗 Esquemático de Hardware

- **ESP8266 (NodeMCU)**
- **BME280**
- Ligações I2C:
  - SDA -> GPIO4 (D2)
  - SCL -> GPIO5 (D1)
- Alimentação 3.3V

## ▶️ Como Executar

1. Instale o firmware MicroPython no seu ESP8266.
2. Use uma ferramenta como **Thonny**, **uPyCraft** ou **ampy** para enviar os arquivos `main.py`, `bme280_float.py` e `request_http.py` para o ESP.
3. Reinicie o ESP. Ele conectará à rede Wi-Fi e começará a enviar dados para a Adafruit IO.

## 🔥 Observações

- O LED do ESP8266 pisca sempre que os dados são enviados com sucesso.
- Caso haja erro na conexão ou no envio, a mensagem será exibida no terminal serial.
- O intervalo entre os envios está definido para 15 segundos. Pode ser alterado no `main.py`:

```python
time.sleep(15)
```

## 📜 Licença

O driver `bme280_float.py` segue a licença MIT, com créditos aos autores originais mencionados no próprio arquivo.

## 💡 Referências

- [Documentação Adafruit IO](https://io.adafruit.com/)
- [Documentação do BME280 - Bosch](https://www.bosch-sensortec.com/)
- [MicroPython Docs](https://docs.micropython.org/)
