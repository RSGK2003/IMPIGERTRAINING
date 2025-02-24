import os
import threading as t
def thread_fib(n,t_name,id):
    a=0
    b=1
    l=[]
    lock=t.Lock()
    lock.acquire()
    for i in range(n):
        l.append(a)
        c=a+b
        a=b
        b=c
    lock.release()
    print(f'Thread_name:{t_name},Output:{l},Thread_id:{id}')
threads=[]
for i in [10,15,20,25,30]:
    thread=t.Thread(target=thread_fib,args=(i,f'Thread{i}',t.get_ident()),name=f'Thread{i}')
    threads.append(thread)
    thread.start()
    thread.join()
# t1=t.Thread(target=thread_fib,args=(10,"T1"))
# t2=t.Thread(target=thread_fib,args=(15,"T2"))
# t3=t.Thread(target=thread_fib,args=(20,"T3"))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
def readanddownloadfiles(src_path,dest_path,f_name):
    with open(src_path,'r') as f:
        content=f.read()
    full_name=os.path.join(dest_path,f_name)
    with open(full_name,'w+') as f:
        f.write(content)
        print(f'File Successfully Downloaded at path {full_name}')
t1=t.Thread(target=readanddownloadfiles,args=('C:/Users/gokulakrishna.ravich/IMPIGERTRAINING/athlete_events.csv',"C:/Users/gokulakrishna.ravich/Downloads/DownloadedFiles",'Download2.txt'))
t2=t.Thread(target=readanddownloadfiles,args=("C:/Users/gokulakrishna.ravich/IMPIGERTRAINING/car_price_dataset.csv","C:/Users/gokulakrishna.ravich/Downloads/DownloadedFiles",'Download3.txt'))
t1.start()
t2.start()
