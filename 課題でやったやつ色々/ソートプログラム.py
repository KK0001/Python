#説明
print("入力された10つの数字を大きい順に並び替えます。\n")

#変数の宣言
a=[]

#入力部分
for i in range(10):
    print(i+1,"つ目の数")
    num=input("=>")
    a.append(int(num))

#ソート部分
a.reverse()

#出力部分
print(a)

