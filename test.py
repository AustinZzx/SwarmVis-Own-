from publish import simplepublish
from publish import rbtpublish
import time

#num = int(raw_input("Enter the number of robots you want to see: "))
rbtpublish(3)
time.sleep(1)
simplepublish("robot2", "end")
