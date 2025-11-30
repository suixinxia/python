import requests
url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
#page = 0


headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
for page in range(0,87):
    print(f'当前页数为{page}')
    params={
    'pageIndex':f'{page}',
    'pageSize':'10',
    }
    response = requests.get(url = url,params=params)
    json_date=response.json()
    #print(json_date)
    lis = json_date['Data']['Posts']
    #print(lis)
    # print(type(lis))
    for li in lis:
        print(li)
print(type(li))







