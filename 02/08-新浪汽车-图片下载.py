import requests,csv
sum_list=[
    ['排名', '车名', '价格', '车型', '热度', '图片链接']
]
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://auto.sina.com.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://auto.sina.com.cn/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}
def down_img(图片链接,车名):
    img_response=requests.get(url=图片链接)
    img_content=img_response.content
    path=f'./图片/{车名}.png'
    with open(path,'wb')as f:
        f.write(img_content)
    print(path,'保存成功')

params = {
    'size': '20',
    'page': '1',
    'dt': '',
    'carGuidePrice': '',
    'serialJiBie': '',
    'corpType': '',
    'ranliaoXingshi': '',
    'serial_id': '',
    'need_detail': '1',
}
url='https://price.auto.sina.com.cn/api/PaihangbangWeibo/serial'
response=requests.get(url=url,params=params,headers=headers)
json_data=response.json()
lis=json_data['data']['list']

for li in lis:
    排名=li['sort']
    车名=li['serial_info']['serialZhName']
    车型=li['serial_info']['serialLevelName']
    图片链接='https'+li['serial_info']['serialWhiteLogo']

    down_img(图片链接,车名)
    热度=li['hot_val']
    价格=li['serial_info']['serialGuidePriceRange']
    if not 价格:
        价格=li['serial_info']['serialPrePriceRange']
        if not 价格:
            价格='未上市'
    d_l=[排名, 车名, 价格, 车型, 热度, 图片链接]
    sum_list.append(d_l)
with open('新浪汽车.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 第一步：创建一个写入对象  传参文件对象
    wr = csv.writer(f)
    # 第二步：写入数据
    wr.writerows(sum_list)






















