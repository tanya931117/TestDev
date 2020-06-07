#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 15:17
# @Author  : tanya
# @File    : my_thread.py
# @Software: PyCharm

from threading import Thread
import time

class mythread(Thread):
    def __init__(self,func,args,name=""):
        # super(mythread, self).__init__(target=func,args=args,name=name)
        Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self) :
        print(self.name+" start")
        self.func(*self.args)
        print(self.name+" end")

def thread_run(value1,value2):
    print(time.ctime()+",value1="+str(value1)+",value2="+str(value2))

if __name__ == "__main__":
    print("主线程启动子线程")
    threads = []
    r = 5
    for i in range(r):
        t = mythread(thread_run,(i,i+1),f"thread{i}")
        threads.append(t)
    for i in range(r):
        threads[i].start()
    for i in range(r):
        threads[i].join()
    print("子线程运行完毕")



