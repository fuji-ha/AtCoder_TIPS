def even_evaluator(x:int)->bool:
    """この関数は引数が偶数ならばTrue,
    奇数ならばFalseを返します
    """
    return x % 2 ==0

#関数の確認
for i in range(5):
    print(i,even_evaluator(i))

#ベースとなるリスト
num_list = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#関数でフィルター
even_list = filter(even_evaluator, num_list)
print(list(even_list))

#lambda でフィルター
even_list2 = filter(lambda x:x % 3 ==0, num_list)
print(list(even_list2))
