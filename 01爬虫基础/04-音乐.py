import requests
music_url = 'https://m804.music.126.net/20251113213854/2b1a74992b66651a9af8f14accf3c851/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/33312727904/43b7/d3f1/b4e1/4cb5deddfea61c9faa740319030310ea.m4a?vuutv=48A1/7+L+48hiNWbTbBYiupQJ26YMf+7+iTDpqtY1MM8hOTlhGy508srui/+4xcEXdQH02vqs6Yb/98McZrEjCsvl/3uxOFaOiK/M7UadtM=&authSecret=0000019a7d59e378043e0a30854e00ad'
response = requests.get(url=music_url)
with open('渐冷.mp3','wb') as f:
    f.write(response.content)








