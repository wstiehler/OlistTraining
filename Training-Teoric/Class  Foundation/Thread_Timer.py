from threading import Timer
from time import sleep

var = True


def hello():
    global var
    print('Hello timer após {} segundos'.format(tempoExec))
    var = False


tempoExec = 2
t = Timer(tempoExec, hello)
t.start()


while var:
    print('hello')
    sleep(0.3)