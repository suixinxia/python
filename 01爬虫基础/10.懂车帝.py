import requests,json
sum_list=[]
for page in range(10):
    #print(f'这是第{page+1}页')
    url =f'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name   =%E4%B8%9C%E8%8E%9E&count=10&offset={page*10}&month=&new_energy_type=&rank_data_type=11&brand_id =&price=&manufacturer=&series_type=&nation=0'
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
        }
    response = requests.get(url= url,headers= headers)
    #print(response.text)
    json_data = response.json()
    #print(json_data['data']['list'])
    lis = json_data['data']['list']
    for li in lis:

        series_name = li['series_name']
        rank = li['rank']
        min_price = li['min_price']
        max_price = li['max_price']
        count = li['count']
        #print(series_name,rank,min_price,max_price,max_price)
        d={
           '名称':series_name,
           '排名':rank,
           '最低价':min_price,
           '最高价':max_price,
           '数量':count,
        }

        sum_list.append(d)
#print(sum_list)
sum_dict={
    '总数据':sum_list
}
print(sum_dict)
with open('懂车帝.json','w',encoding='utf-8') as f:
    json.dump(sum_dict, f, ensure_ascii=False, indent=4)


with open('懂车帝.json','r',encoding='utf-8') as f:
    a = json.load(f)

print(a['总数据'][0])









