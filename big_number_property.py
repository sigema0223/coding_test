n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

num = 0
number1 = data[n-1]
number2 = data[n-2]

result = 0
for i in range(m):
    for j in range(k):
        result += number1
        num += 1
        if num == m: break
    result += number2
    num += 1
    if num == m: break

print(result)