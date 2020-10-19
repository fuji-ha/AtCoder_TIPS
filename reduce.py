from functools import reduce

def func(x, y):
    return x * y

list_a = [100, 20, 30,10]

print(reduce(func, list_a))

b= reduce(lambda x, y: x - y, list_a)
print(b)