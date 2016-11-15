import random

def make_random_array(size):
    arr=list()#配列の容易
    for v in range(size):
        arr.append(random.randint(0,1003))
    return arr

a=int(input("整数を入力:"))
result=make_random_array(a)
print(result)
