import threading
import time

def ism1():
    for x in range(30):
        time .sleep(0.2)
        print("sevarabonu")

def familiya2():
    for x in range(30):
        time.sleep(0.2)
        print("sharopova")

def achistva3():
    for x in range(30):
        time.sleep(0.2)
        print("shoyim qizi")

s1 = threading.Thread(target=ism1)
s2 = threading.Thread(target=familiya2)
s3 = threading.Thread(target=achistva3)

s1.start()
s2.start()
s3.start()


