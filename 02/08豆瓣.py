import requests,csv
from lxml import etree
list=[
    ['电影名','电影排名','电影评分','电影导演','电影简介']
]
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }
for page in range(11):
    url=f'https://movie.douban.com/top250?start={page*25}&filter='
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    html_content=response.text
    tree=etree.HTML(html_content)
    #print(html_content)
    dy_name=tree.xpath("//div[@class='hd']/a/span[1]/text()")
    #print(dy_name)
    for i1 in dy_name:
        a1=i1
    dy_pm=tree.xpath("//div[@class='pic']/em/text()")
    #print(dy_pm)
    for i2 in dy_pm:
        a2=i2


    dy_pf=tree.xpath("//span[@class='rating_num']/text()")
    #print(dy_pf)
    for i3 in dy_pf:
        a3=i3
        #print(i)
    dy_dy=tree.xpath("//div[@class='bd']/p/text()")
    #print(dy_dy)
    dy_metho="".join(dy_dy).replace(' ','').replace('/n','').replace('/t','')
    #print(dy_metho)
    dy_jj=tree.xpath("//div[@class='bd']/p[2]/span/text()")
    #print(dy_jj)
    for i4 in dy_jj:
        a4=i4
    li=[a1,a2,a3,dy_metho,a4]
    list.append(li)
with open('豆瓣T250.csv','w',encoding='utf-8-sig',newline='')as f:
    wr = csv.writer(f)
    wr.writerows(list)










