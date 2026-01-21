import threading
import time

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    #sing()
    #dance()
    sing_thread = threading.Thread(target=sing, args=("I'm singing",)) #singing thread
    dance_thread = threading.Thread(target=dance, kwargs = {"msg": "I'm dancing"}) #dancing thread

    sing_thread.start()
    dance_thread.start()