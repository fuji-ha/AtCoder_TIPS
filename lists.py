lists = [1,2,3,4,5]
print(lists)
print(*lists,sep="")
for i in lists:
    print(i,end="-")
print()
print([i for i in lists])
