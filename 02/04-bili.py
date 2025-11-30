import requests
url= 'https://www.bilibili.com'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36','referer':'https://www.bilibili.com/bangumi/play/ep11511?from_spmid=666.25.episode.0'
}
response=requests.get(url=url,headers=headers)
print(response.content)
# with open('学生会的一己之见.mp4','wb')as f:
#     f.write(response.content)











