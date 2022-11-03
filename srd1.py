import threading as t
import time 
def func1():
    for x in range(0,70):
        time.sleep(0.3)
        print(x)

def func2():
    for x in range(0,70):
        time.sleep(0.3)
        print(x)
func1()
func2()