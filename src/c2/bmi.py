# #BMI判定プログラム
# weight = float(input("体重(kg)は ? "))
# height = float(input("身長(cm)は ? "))
# # BMIの計算
# height = height / 100 # m に直す
# bmi = weight / (height * height)
# # BMIの値に応じて結果を分岐 --- (*1)
# result = ""
# if bmi < 18.5:
#     result = "痩せ型"
# if (18.5 <= bmi) and (bmi < 25):
#     result = "標準体重"
# if (25 <= bmi) and (bmi < 30):
#     result = "肥満(軽)"
# if bmi >= 30:
#     result = "肥満(重)"
# # 結果を表示
# print("BMI :", bmi)
# print("判定:", result)


# #BMI判定プログラム
weight = float(input("体重(kg)は？"))
height = float(input("身長(cm)は？"))

#BMIの計算
height = height / 100 
bmi = weight / (height * height)

#結果に応じて分岐
result = ""
if bmi < 18.5:
    result = "痩せ型"
if (18.5 <= bmi)and(bmi<25):
    result = "普通体重"
if (25 <= bmi) and (bmi < 30): #25 <= bmi <30 と同じ意味
    result = "肥満(軽）" 
if 30 < bmi:
    result ="肥満(重）"

#結果
print ("あなたのbmiは{0}で、判定は{1}です".format(bmi,result))


