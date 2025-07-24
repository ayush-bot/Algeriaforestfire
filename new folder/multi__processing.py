import multiprocessing

import time

def square():
    for i in range(5):
        print(f"square: {i*i}")
        time.sleep(2)
def cube():
    for i in range(5):
        print(f"cube: {i*i*i}")
        time.sleep(2)

if __name__=="__main__":

    t1=multiprocessing.Process(target=square)
    t2=multiprocessing.Process(target=cube)

    before=time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    After=time.time()-before

    print(After)