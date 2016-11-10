from publish import *
import time
import thread


try:
   thread.start_new_thread( rbtpublishseperate, ("robot1", "robot2", ) )
   thread.start_new_thread( rbtpublishseperate, ("drone1", "robot1", ) )
except:
   print "Error: unable to start thread"
while 1:
   pass
time.sleep(1)
simplepublish("robot1", "end")
