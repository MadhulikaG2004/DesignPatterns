from threading import Thread
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print(f"Hello {i+1}")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print(f"Hi {i+1}")
            sleep(1)

if __name__=="__main__":
    
    t1=Hello()
    t2=Hi()

    t1.start()
    t2.start()