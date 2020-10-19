from functools import reduce

# 利用例1
def func(x, y):
    return x * y

list_a = [100, 20, 30,10]

print(reduce(func, list_a))

#利用例2
b= reduce(lambda x, y: x + y, list_a)
print(b)