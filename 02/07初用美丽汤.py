import requests
from bs4 import BeautifulSoup
url='https://www.bilibili.com/'
headers={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
}
response = requests.get(url=url,headers=headers)
html_doc=response.text
print(response.text)
soup=BeautifulSoup(html_doc,'lxml')
print(soup.title.string)
# for link in soup.find_all('a'):
#     print(link.get('href'))
#print(soup.get_text())














