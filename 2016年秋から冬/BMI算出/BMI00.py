#入力
a=float(input("あなたの体重(kg):"))
b=float(input("あなたの身長(m):"))
BMI=a/(b**2)#BMIです。

#出力
print("BMIは"+str(BMI)+"です。")
if BMI<18.5:
    print("痩せています。")
elif 18.5<=BMI<25:
    print("普通です。")
elif 25<=BMI<35:
    print("少し太っています。")
elif 35<=BMI:
    print("太っています。")
