import requests
img_url = "https://haowallpaper.com/link/common/file/previewFileImg/17873560258071936"

response= requests.get(url=img_url)

print(response.content)
with open ('美女.jpg','wb') as f:
    f.write(response.content)





