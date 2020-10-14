class Cat:
    # クラス変数
    nakigoe = "nya-" #クラス変数名 = 値
    # メソッド
    def naku(self):
        print(Cat.nakigoe) #print(クラス名.クラス変数名)

mike = Cat() #Catクラスでmikeというインスタンスを生成。
mike.naku() # nya-

nora = Cat() #Catクラスでnoraというインスタンスを生成。
nora.naku() # nya-

# ここでクラス変数を変更する
Cat.nakigoe = "myu-" #クラス名.クラス変数名 = 新しい値

# すると全てのインスタンスで値が変更される
nora.naku() # myu-
mike.naku() # myu-

# 再びクラス変数を変更する
Cat.nakigoe = "mya-" #クラス名.クラス変数名 = 新しい値

# すると全てのインスタンスで値が変更される
nora.naku() # mya-
mike.naku() # mya-



