class Student:
    ''' 生徒を表すクラス '''
    def __init__(self, id, name, score = 0): #score初期値は0
        ''' 初期化 '''
        self.id = id
        self.name = name
        self.score = score
        
    def getId(self):
        ''' IDを取得するメソッド '''
        return self.id
        
    def getName(self):
        ''' 生徒名を取得するメソッド '''
        return self.name
        
    def setScore(self, score):
        ''' 点数を設定するメソッド '''
        self.score = score
        
    def getScore(self):
        ''' 点数を取得するメソッド '''
        return self.score

class CalcScore:
    ''' 点数を計算する関数 '''
    def __init__(self):
        ''' 初期化 '''
        self.students = [] #空のリスト
        
    def addStudent(self, student):
        ''' 学生を追加する '''
        self.students.append(student) #slef.studentsリストに、studentプロパティを追加

    def ave(self):
        v = 0
        for i in self.students: #リストの分だけiをループ
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v

# 学生を表すインスタンスを生成
p1 = Student(10, "佐藤")
p1.setScore(80) #p1に、80点のスコアを追加
p2 = Student(11, "鈴木", score=79)
p3 = Student(12, "佐々木", score=84)
p4 = Student(13, "井上", score=77)

# 平均点を計算
calc = CalcScore() #CalcScoreクラスでcalcインスタンスを生成
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点=", calc.ave())

# print(type(p1))  →結果<class '__main__.Student'> Student型と表示。
print(f"ID:{p1.id} \n氏名:{p1.name} \nスコア:{p1.score}") #値取得の練習。インスタンス名.プロパティ名で取得可能。　\nは改行
