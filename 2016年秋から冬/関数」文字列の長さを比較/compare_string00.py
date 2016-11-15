def compare_string(a,b):
    if len(a)>len(b):
        return a
    return b

str1=input("文字列1を入力:")
str2=input("文字列2の入力:")

result=compare_string(str1,str2)
print("長い方は:",result)
