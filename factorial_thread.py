# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:23:24 2018

@author: python
"""

import threading
import math 
import numpy as np

N=10;
v1=np.arange(N,0);
v2=np.arange(N,1); 
v11=[];
v12=[];
suma=0; 

def factorial(vec):
    global suma
    for i in vec:
        fac = math.factorial(i)
        print vec2
    return suma;    
#haremos la suma parcial     
for i in range(4):
    t1 =threading.Thread(target = factorial, args=(v1,))
    t2 =threading.Thread(target = factorial, args=(v2,))
    #su target es la funcion fuction
    t1.start();t2.start()
    t.join();t2.join()    