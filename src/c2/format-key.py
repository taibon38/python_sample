# (1) 
print("私は{name}です。".format(name="ミドリ"))
print("私こそ{hero}だ。".format(hero="アイアンマン"))

# (2)
fmt = "年齢は、{age}才で、{job}をやってます。"
s = fmt.format(age=22, job="プログラマー")
print(s)

fmt2 = "普段は、{job}で、{work}をやってます。"
t = fmt2.format(job="経営者" , work="武器づくり")
print(t)