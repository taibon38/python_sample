# # ダイアログを表示するために必要なモジュール --- (*1)
# import tkinter.messagebox as mb

# # ダイアログを表示 --- (*2)
# ans = mb.askyesno("質問", "ラーメンは好きですか？")
# if ans == True:
#     # OKボタンがあるだけのダイアログを表示 --- (*3)
#     mb.showinfo("同意", "僕も好きです。")
# else:
#     mb.showinfo("本当？", "まさか、ラーメンが嫌いだなんて!")

# 練習

import tkinter.messagebox as mb

ans = mb.askyesno("質問です！","ラーメンは好きですか？") #YesかNoで答える質問ダイアログを表示 askyesno(タイトル、メッセージ)
if ans == True:
    mb.showinfo("同意です。","僕は一風堂が好きです") #OKボタンが配置されただけの情報ダイアログを表示
else:
    mb.showinfo("まさか！","今度一緒に行きましょう。")

# ダイアログの種類
ans = mb.askokcancel("質問です！","ラーメンは好きですか？") #OKかキャンセルのボタンを持つダイアログ
if ans == True:
    mb.showerror("同意です。","僕は一風堂が好きです") #OKボタンを持つエラーダイアログ
else:
    mb.showwarning("まさか！","今度一緒に行きましょう。") #OKボタンを持つ警告ダイアログ