from machine import UART
import time

# UART1 -> TX=D1 (GPIO5), RX=D2 (GPIO4)
uart = UART(1, baudrate=9600, tx=1, rx=3)


print("Iniciando leitura do GPS...\n")

try:
    if uart.any():
        line = uart.readline()
        print("Entrou no If..\n")
        if line:
            try:
                decoded = line.decode('utf-8')
                print("Decodificou..\n")
                if decoded.startswith('$GPRMC') or decoded.startswith('$GPGGA'):
                    print(decoded.strip())
            except UnicodeError:
                print("Linha inválida.")
    time.sleep(0.2)
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")