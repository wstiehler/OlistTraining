import threading
from time import sleep


def wait():
    count = 0
    while True:
        print(count)
        count +=1
        sleep(0.1)


t = threading.Thread(target=wait, name='wait', daemon=True)
t.start()
print(threading.enumerate()[1].is_alive())#Se esta ativa. Retorna true ou False
sleep(1)
print(t.is_alive())









