
import multiprocessing
import time


def square_list(mylist, Actor, square_sum):
    sum = 0
    for idx, num in enumerate(mylist):
        sum += num * num
        time.sleep(0.1)
        square_sum.value += num * num


n = 30
mylist = [i for i in range(n)]


result = multiprocessing.Array('i', n)
square_sum = multiprocessing.Value('i')
square_sum.value = 0

p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

p1.start()



#print(result[:])

t1 = time.time()
for _ in range(n):
    print(square_sum.value)
    square_sum.value *= 1
    time.sleep(0.1)
t2 = time.time()

print('time used:', t2-t1)


p1.join()
print(square_sum.value)