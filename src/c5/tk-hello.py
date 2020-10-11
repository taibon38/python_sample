# tkinterを取り込む --- (*1)
from tkinter import *
import tkinter.messagebox as mb

# ボタンが押された時の動作を関数として定義 --- (*2)
def say_hello():
    mb.showinfo("挨拶","おはようございます") #OKボタンがあるだけのダイアログ

# メインウィンドウを作成 --- (*3)
root = Tk() #rootは変数名なので決まりは特になし。Tk()は、2行目でインストールしているため利用できている。TKというクラスからインスタンスをつくる。
root.title('挨拶') # メインウィンドウのタイトルを設定 TK()でつくられたインスタンスに.titleのメソッドを使っている。

# ラベルを作成 --- (*4)
desc_label = Label(text="以下のボタンを押してください") # ラベル=Tkinterにおけるテキスト
desc_label.pack() #pack()メソッドで、メインウィンドウ上に配置　

# 挨拶ボタンを作成 --- (*5)
hello_button = Button(
    text="挨拶",        # ボタンのテキスト
    width=10, height=3, # 文字数でボタンのサイズを指定
    command=say_hello   # ボタンをクリックした時の動作
)
hello_button.pack()

# メインループを開始 --- (*6)
root.mainloop()

