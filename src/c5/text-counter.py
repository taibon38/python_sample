# # tkinterをインポート --- (*1)
# from tkinter import *

# # テキストの文字数を数える関数 --- (*2)
# def count_text(event):
#     s = main_text.get(1.0, END) #辞書型.get(キー,キーが存在しない場合の返り値)
#     info_label.config(text="{0}文字".format(len(s)))

# # メインウィンドウを作成 --- (*3)
# root = Tk()
# root.title('テキストカウンタ')

# # テキストボックスを作成 --- (*4)
# main_text = Text(root)
# main_text.bind("<Key>", count_text) # イベントを設定 --- (*5)  キーボードからキーを入力したときに、count_text関数が実行されるように設定。
# main_text.pack()

# # 文字数を表示するラベルを作成 --- (*6)
# info_label = Label(root)
# info_label.pack()

# # メインループ --- (*7)　イベントループというもので、マウスクリックやキーボードからの入力のこと。
# root.mainloop()

from tkinter import * # from モジュール名 import オブジェクト名

def count_text(event):
    s = main_text.get(1.0,END)
    info_label.config(text="{0}文字".format(len(s)))

root = Tk()
root.title('テキストカウンターです')


info_label = Label(root) # コードの位置で上下が変わる。
info_label.pack()

main_text = Text(root)
main_text.bind("<Key>",count_text)
main_text.pack()

root.mainloop()