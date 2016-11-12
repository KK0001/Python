class MyClass(object):
    # クラス直下に定義した変数はクラス変数
    # インスタンス変数ではなく、Javaをやっていた身としては混乱しやすい
    # some_field = "aaa"

    # インスタンス生成時に、値を渡すことができる
    def __init__(self, name, age):
        # 「self.xxx」でインスタンス変数の参照/代入ができる
        self.name = name
        self.age = age

    # インスタンスメソッドの定義
    def introduce(self):
        print("My name is",self.name,",",self.age,"years old." )    #結果を出力(print)
        print("My name is %s, %d years old."%(self.name, self.age)) #このような表示方法を初めて知ったのでついでに。

# インスタンス化
a=input("名前は何ですか？→ ")
b=int(input("何歳ですか？→ "))
me = MyClass(a, b)
print(me.introduce())

"""
http://www.yoheim.net/blog.php?q=20160405
を参考
"""
