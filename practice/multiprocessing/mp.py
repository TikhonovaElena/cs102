import os
import time
import psutil
from multiprocessing import Process
 
 
def doubler(number):
    """
    Функция умножитель на два
    """
    start_time = time.time()
    result = number ** 10000
    proc = os.getpid()
    py = psutil.Process(proc)
    memory_use = py.memory_info()
    print('py = {}'.format(py))
    print('memory_use = {}'.format(memory_use))
    print('{0} doubled to by process id: {2}. I need {3} s for it\n'.format(
        number, result, proc, time.time() - start_time))
 
 
if __name__ == '__main__':
    numbers = [1069, 3001, 7233, 51, 25]
    procs = []

    all_time = time.time()
    
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print('all time is {} s'.format(time.time() - all_time))