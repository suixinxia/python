import requests,csv
from lxml import etree
url='https://top.zol.com.cn/compositor/57/cell_phone.html'


# cookies = {
#     'ip_ck': '78aJ7/v+j7QuODE4ODE5LjE3NjQxNDMyNjY%3D',
#     'lv': '1764143266',
#     'vn': '1',
#     'Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0': '1764143267',
#     'HMACCOUNT': 'BC1032A5B6BF9C3E',
#     'z_pro_city': 's_provice%3Dguangdong%26s_city%3Ddong',
#     'Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0': '1764143313',
#     'z_day': 'icnmo11564=1&rdetail=1',
#     'realLocationId': '9',
#     'userFidLocationId': '9',
#     'm_area_city_new': 'dong',
#     'm_area_cityId_new': '354',
#     'm_area_provinceId_new': '30',
#     'questionnaire_pv': '1764115202',
# }
sum_list=[
    ['型号','价格','评分','图片链接']
]
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Wed, 26 Nov 2025 07:33:40 GMT',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
     'cookie': 'ip_ck=78aJ7/v+j7QuODE4ODE5LjE3NjQxNDMyNjY%3D; lv=1764143266; vn=1; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1764143267; HMACCOUNT=BC1032A5B6BF9C3E; z_pro_city=s_provice%3Dguangdong%26s_city%3Ddong; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1764143313; z_day=icnmo11564=1&rdetail=1; realLocationId=9; userFidLocationId=9; m_area_city_new=dong; m_area_cityId_new=354; m_area_provinceId_new=30; questionnaire_pv=1764115202',
}

response = requests.get(url=url, headers=headers,verify=False)
html=response.text
#print(html)
tree=etree.HTML(html)
list_data1=tree.xpath('.//div[@class="rank__name"]/a/text()')
list_data=tree.xpath('.//div[@class="rank-list__item clearfix"]')
#print(list_data)

list_data2=tree.xpath('.//img/@src')
#print(list_data2)
list_data3=tree.xpath('.//div[@class="rank__price"]/text()')
#print(list_data3)
list_data4=tree.xpath('.//div[@class="score clearfix"]/span/text()')
#print(list_data4)
for li in list_data:
    list_data1 = li.xpath('.//div[@class="rank__name"]/a/text()')[0]
    list_data2 = li.xpath('.//img/@src')[0]
    #print(list_data2)
    list_data3 = li.xpath('.//div[@class="rank__price"]/text()')[0]
    #print(list_data3)
    list_data4 = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].replace('分','')
    #print(list_data4)
    sum_li=[list_data1,list_data3 ,list_data4,list_data2]
    sum_list.append(sum_li )
with open('热门手机排行.csv','w',encoding='utf-8-sig',newline='')as f:
    wr = csv.writer(f)
    wr.writerows(sum_list )


