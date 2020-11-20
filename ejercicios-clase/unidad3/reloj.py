# 08:49:49 PM
import time

while True:
    hora_actual = time.localtime()
    reloj = time.strftime("%I:%M:%S %p", hora_actual)
    print(reloj, end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
