# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:00:00 2018

@author: python
"""

import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter


    def run(self):
        print( "Starting " + self.name)
        print_date(self.name, self.counter)
        print( "Exiting " + self.name)


        
def print_date(threadName, counter):
    print( "%s[%d]: %s" % ( threadName, counter, time.time()))

        
    # Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting the Program!!!")