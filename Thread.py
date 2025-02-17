import time
from threading import *
# def thread_process(num,sleeptime,name):
#     for i in range(num):
#         print(name,i)
#         time.sleep(1)
# t1=threading.Thread(target=thread_process,args=(3,1,"one"))
# t1.start()
# t2=threading.Thread(target=thread_process,args=(2,1,"Two"))
# t2.start()
# l=threading.Lock()
# def lockandunlock(d):
#     l.acquire()
#     execute(d)
#     l.release()
# def execute(d):
#     for i in range(5):
#         print(d)
# t3=threading.Thread(target=lockandunlock,args=("Hi",))
# t4=threading.Thread(target=lockandunlock,args=("Hello",))
# t3.start()
# t4.start()
# t3.join()
# t4.join()
# s=Semaphore(2)
# def source(d):
#     s.acquire()
#     print(d)
#     s.release()
# for i in range(5):
#     t=Thread(target=source,args=(f'hi{i}',))
#     t.start()
#TASK
def t_main():
    print("This is process 1")
    t1=Thread(target=process2,args=())
    t2=Thread(target=process3,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
def process2():
    print('This is process 2')
def process3():
    print('This is process 3')
t3=Thread(target=t_main,args=())
t4=Thread(target=process2,args=())
t5=Thread(target=process3,args=())
t3.start()
t4.start()
t5.start()
t3.join()
t4.join()
t5.join()

