# 成績データを辞書型で定義
records = { 
    'Tanaka':72, 'Yamada':65, 'Hirata':100, 
    'Akai':56, 'Fukuda':66, 'Sakai':80 }
# # 合計を求める --- (*1)
# sum_v = 0
# for v in records.values():
#     sum_v += v
# # 平均点を計算して結果を表示
# ave_v = sum_v / len(records)
# print("合計点:", sum_v)
# print("平均点:", ave_v)

# # 成績データの一覧と平均点との差を表示 --- (*2)
# fmt = "| {0:<7} | {1:>4} | {2:>5}"
# print("| 名前    | 点数 | 差")
# for name, v in sorted(records.items()):
#     # 平均点との差を求める
#     diff_v = v - ave_v 
#     # 小数点以下を丸める --- (*3)
#     diff_v = round(diff_v, 1)
#     # 書式にそって出力 --- (*4)
#     print(fmt.format(name, v, diff_v))


sum_v = 0
for v in records.values():
    sum_v += v
ave_v = sum_v / len(records)
print("合計は",sum_v,"点")
print("平均は",ave_v,"点")

fmt = "|{0:<7}|{1:>4}|{2:>5}"
print("|名前   |点数| 差")
for name , v in sorted(records.items()):
    diff_v = v - ave_v
    diff_v = round(diff_v,1)
    print(fmt.format(name,v,diff_v))
