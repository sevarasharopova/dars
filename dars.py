import threading
import time
from ism import *
from f import *
from sh import *

s1 = threading.Thread(target=ism)
s2 = threading.Thread(target=familiya)
s3 = threading.Thread(target=sharif)

s1.start()
s2.start()
s3.start()

