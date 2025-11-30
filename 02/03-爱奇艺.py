import requests,jsonpath,json
sum_list=[]
url = 'https://mesh.if.iqiyi.com/portal/pcw/rankList/comSecRankList?v=13.084.0&device=c2de58c05f5096d3898dc0b7865d09fc&auth=&uid=&ip=202.108.14.240&refresh=0&server=false&page_st=0&tag=0&category_id=-1&channelId=0&date=&pg_num=2&next_pos='

headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
#print(response.text)
json_data=response.json()
#print(json_data)
title_list=jsonpath.jsonpath(json_data,'$..title')
tags_list=jsonpath.jsonpath(json_data,'$..tags')
desc_list=jsonpath.jsonpath(json_data,'$..desc')
mainIndex_list=jsonpath.jsonpath(json_data,'$..mainIndex')
#print(title_list,tags_list,desc_list,mainIndex_list)
for i in zip(title_list,tags_list,desc_list,mainIndex_list):
    #print(i)
    d={
       '影片名称':i[0],
       '影片标签':i[1],
       '影片简介':i[2],
       '影片热度':i[3]
    }
    sum_list.append(d)
sum_dict={
    "总数据":sum_list
}
with open('爱奇艺热播.json','w',encoding='utf-8')as f:
    json.dump(sum_dict,f,ensure_ascii=False,indent=4)


















