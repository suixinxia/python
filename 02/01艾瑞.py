import requests,json
sum_list=[]
for page in range(10):
    url  = f'https://index.iresearch.com.cn/app/GetDataList1?classId=0&classLevel=0&timeId=202509&orderBy=2&pageIndex={page}&pageSize=10'
    # https://index.iresearch.com.cn/app/GetDataList1?classId=0&classLevel=0&timeId=202509&orderBy=2&pageIndex=2&pageSize=10
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }
    response = requests.get(url = url,headers=headers)
    #print(response.text)
    json_data=response.json()
    #print(json_data['List'])
    for li in json_data['List']:
        AppName=li['AppName']
        Rank=li['Rank']
        FclassName=li['FclassName']
        KclassName=li['KclassName']
        UseNum=li['UseNum']
        Growth=li['Growth']

        d={
            '名称':AppName,
            '排名':Rank,
            '类别':f'{FclassName}-{KclassName}',
            '独立设备数':UseNum,
            '环比增幅(%)':Growth
          }
        #print(d)
        sum_list.append(d)

#print(sum_list)
sum_dict={
    '总数据':sum_list
}
with open('艾瑞APP.json','w',encoding='utf-8')as f:
    json.dump(sum_dict,f,ensure_ascii=False,indent=4)