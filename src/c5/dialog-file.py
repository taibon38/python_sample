# # ダイアログを表示するために必要なモジュール 
# import tkinter.filedialog as fd

# # ファイル選択ダイアログを表示する
# path = fd.askopenfilename(
#     title="処理対象のファイルを指定してください",
#     filetypes=[('HTML','.html')]) # [(ラベル、パターン),(ラベル,パターン)...]というタプルのリストを与える。
# print(path)

# 練習
import tkinter.filedialog as fd
path_py = fd.askopenfilename(
    title = "処理対象のPythonファイルを指定してください" ,
    filetypes=[('Python','.py')])
print(path_py)