# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 08:36:22 2018

@author: python
"""
from threading import Thread				

class threads_object(Thread):
    def run(self):
        function_to_run()
#llamamos a la funcion function_to_run
# por que los threads corren como instancias
        

def threaded():
    funcs = []
    for i in range(4):
        funcs.append(threads_object())
        #genera los hilos 
    for i in funcs:
        i.start()
        #arranca los hilos
        #estas funciones se heredan del Thread
    for i in funcs:
        i.join()
        # se espera y los junta
#genera objetos con distintos hilos de ejecucion        
#corre la funcion un numero de veces (num_threads)
# que sera  1 2 4 8 usando ese numero de procesadores
        
def function_to_run():
    import urllib.request
    for i in vector:
        r= urllib.request.get(i);
        st=r.status_code    
#descarga los 126 primeros bits de la url 10 veces
            
def show_results(func_name, results):
    print ("%-23s %4.6f seconds" % (func_name, results))

if __name__ == "__main__":
    import sys
    from timeit import Timer			
    repeat = 1
    number = 1
    Urls = [ "http://httpbin.org/status/418","http://httpbin.org/status/404","http://httpbin.org/status/200","http://httpbin.org/status/500"]
    print ('Starting tests')
    for i in Urls:			
        t = Timer("threaded(%s)" %i, "from __main__ import threaded")
        best_result =  min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)
print ('Iterations complete')
#compara los resultados

#entrada y salida de info es mejor con threads 
#