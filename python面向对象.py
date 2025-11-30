class me():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'{self.name}已经{self.age}岁了')#定义对象自动执行
    def method(self):#类方法
        print('I can fly')
    def run(self):
        self.method()
class he(me):
    def anime(self):
        print('爱看动漫')
    def sports(self):
        print('爱打篮球')
    def method(self):
        print("hello")
        super().method()#既用父类也用子类
a=me('罗先豪',19)
b=he('帅哥',30)
a.run()
b.run()
# b.method()方法相同会覆盖
b.method()



















