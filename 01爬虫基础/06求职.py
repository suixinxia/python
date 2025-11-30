import requests
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1763265307607&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
response = requests.get(url= url)

print(response.encoding)
print(response.text)
print(type(response.text))
print(response.json())
print(type(response.json()))


