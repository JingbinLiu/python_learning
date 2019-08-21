
import multiprocessing
import time


def square_list(q):
    for num in range(10):
        time.sleep(0.1)
        print('qsize()', q.qsize())
        q.put(num * num)
        print('q.put()', num * num)


def print_list(q):
    while True: #not q.empty():
        time.sleep(2)
        print('q.get()', q.get())


q = multiprocessing.Queue(2)

p1 = multiprocessing.Process(target=square_list, args=(q,))
p2 = multiprocessing.Process(target=print_list, args=(q,))

p1.start()
time.sleep(0.1)
#p2.start()


while True:  # not q.empty():
    time.sleep(2)
    print('q.get()', q.get())


p1.join()
#p2.join()

