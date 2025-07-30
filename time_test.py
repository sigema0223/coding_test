from random import randint
import time

array = []
for i in range(1000):
    array.append(randint(1,100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()

result_time1 = end_time - start_time
print("selection sort time consumption : ", result_time1)

array = []
for i in range(1000):
    array.append(randint(1,100))

start_time = time.time()

array.sort()

end_time = time.time()

result_time2 = end_time - start_time
print("array.sort() time consumption : ", result_time2)

print("selection sort is fast" if result_time1 < result_time2 else "array.sort() is fast")


