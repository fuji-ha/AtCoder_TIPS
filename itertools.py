import itertools
x = [1,2,3]
y = [4,5,6]
xy = itertools.product(x,y)
for i in xy:
    print(i[0],i[1],end=" | ")



