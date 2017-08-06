# -*- coding: gbk -*-  
#coding=gbk 

import thread,time,random  
dish=0 
lock = thread.allocate_lock()  
def producerFunction():  
   global lock,dish  
   while True:  
       if(random.random() > 0.1):  
         lock.acquire()  
         if dish < 100:  
           dish+=1  
           print('up%d'%(dish,))  
         lock.release()  
         time.sleep(random.random()*3)  
  
def consumerFunction():   
  global lock,dish  
  while True:  
    if(random.random() > 0.9):  
      lock.acquire()  
      if dish > 0:  
        dish-=1  
        print('down%d'%(dish,))  
      lock.release()  
      time.sleep(random.random()*3)  
  
def begin():  
  ident1=thread.start_new_thread(producerFunction,())  
  ident2=thread.start_new_thread(consumerFunction,())  
if __name__ == '__main__':  
  begin()
  while 1:
   pass