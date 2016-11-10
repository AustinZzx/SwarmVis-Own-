from publish import *
import time
import thread


try:              #using threads to publish positions for various robots
   thread.start_new_thread( rbtpublishseperate, ("car1", "robot2", ) )
   thread.start_new_thread( rbtpublishseperate, ("drone1", "robot1", ) )
   thread.start_new_thread( rbtpublishseperate, ("car2", "robot3", ) )
   thread.start_new_thread( rbtpublishseperate, ("drone3", "robot4", ) )
except:
   print "Error: unable to start thread"
while 1:
   pass
time.sleep(1)
simplepublish("robot1", "end")

#this extremely relies on the Internet condition
