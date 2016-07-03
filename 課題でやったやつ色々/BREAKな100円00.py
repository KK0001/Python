print("100円の崩し方大全。")
print("50　10　5　1")
count=0
for l in range(3):
    for m in range(11):
        for n in range(21):
            for o in range(101):
                if(50*l+10*m+5*n+1*o==100):
                    count+=1
                    print(l," ",m," ",n," ",o)
print("組み合わせ総数は",count,"だよ")