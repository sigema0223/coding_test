import ast

s = input("Enter a literal(e.g [1,2,3,4] or {'a':1,'b':2}): ")
data = ast.literal_eval(s)

print(type(data), data)

nums = list(map(int, input("Enter integers separated by spaces: ").split()))
print(type(nums), nums)