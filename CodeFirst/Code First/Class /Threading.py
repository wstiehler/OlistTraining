import threading
from time import sleep


def wait():
    sleep(2)
    print('Acabou')


class myThread(threading.Thread):
    def __init__(self, target, name='myThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = myThread(wait)
t.start()
print(t.name)










#Funciona uma "agrarrando" a outra.
#t1 = threading.Thread(target=wait, name='wait', daemon=True)
#t1.start()
#print(t1.is_alive())
#print(t1.name)


#t2 = threading.Thread(target=wait, name='wait')
#t2.start()
#print(t2.is_alive())
#print(t2.name)







