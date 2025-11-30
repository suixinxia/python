import csv
data=[
    ['姓名','年龄','城市'],
    ['小明','10','四川'],
    ['小红','12','上海']
]
with open('1.csv','w',encoding='utf-8-sig',newline='')as f:
    wr = csv.writer(f)
    wr.writerows(data)


fieldnames =['姓名','年龄','性别']
# 定义要写入的数据
data =[
{'姓名':'张三','年龄':25,'性别':'男'},
{'姓名':'李四','年龄':30,'性别':'女'}
]
with open('1.csv','w',encoding='utf-8-sig',newline='')as f:
    r=csv.DictWriter(f,fieldnames)
    r.writeheader()
    r.writerows()





