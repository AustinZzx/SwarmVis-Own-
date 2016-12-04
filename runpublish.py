from publish import *
import time
import thread

simplepublish("subscribe", "robot1 car")
simplepublish("subscribe", "robot2 drone")
simplepublish("subscribe", "robot3 car")
simplepublish("subscribe", "robot4 drone")

try:              #using threads to publish positions for various robots
   thread.start_new_thread( rbtpublishseperate, ("thread1", "robot1", ) )
   thread.start_new_thread( rbtpublishseperate, ("thread2", "robot2", ) )
   thread.start_new_thread( rbtpublishseperate, ("thread3", "robot3", ) )
   thread.start_new_thread( rbtpublishseperate, ("thread4", "robot4", ) )
except:
   print "Error: unable to start thread"
while 1:
   pass
time.sleep(1)
simplepublish("subscribe", "end")

#this extremely relies on the Internet condition
