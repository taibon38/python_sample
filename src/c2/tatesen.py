# 画面に300本の縦線を引く

# グラフィックライブラリを取り込む
from tkinter import *
# 画面の初期化
w = Canvas(Tk(), width=500, height=500)
w.pack()

# 線をたくさん引く ---- (*1)
for i in range(300):
    x = i * 3
    w.create_line(x, 0, x, 500, fill="#000000")

mainloop()

