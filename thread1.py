# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:23:24 2018

@author: python
"""

import threading
def function(i):
    print("function called by thread %i \n"%i);
    return
for i in range(5):
    t =threading.Thread(target = function, args=(i,))
    #su target es la funcion fuction
    t.start()
    t.join()    