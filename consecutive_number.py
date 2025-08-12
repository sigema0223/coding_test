n, m, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0
data.sort()
first_number = data[n-1]
second_number = data[n-2]

#This code has a complexity as O(nlogn+m) but we can decrease it to O(nlong).
"""
while True:
    for i in range(k):
        if m == 0:
            break
        result += first_number
        m -= 1
    if m == 0:
        break
    result += second_number
    m -= 1
"""

#This one has O(nlogn)
count = ((m//(k+1))*k+m%(k+1))
result = count*first_number+(m-count)*second_number


print(result)