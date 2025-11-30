import requests
bili_url = 'https://www.bilibili.com/'
headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
'cookie':
"buvid3=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc; b_nut=1763263021; _uuid=5D96A149-2918-10862-2726-A104AEC9D6141021728infoc; buvid4=7070262B-D05B-3887-524D-1E8A23B23A1822240-025111611-sSA5PGJPu868bv+N1mqzCQ%3D%3D; buvid_fp=df0d40d01dc665444357cbfb49fc7af7; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjM1MjIyMjIsImlhdCI6MTc2MzI2Mjk2MiwicGx0IjotMX0.g_5mNuzgWYYHUOgJhLJW-ihm7D-_oVKmbCk0PU-oLPo; bili_ticket_expires=1763522162; CURRENT_QUALITY=0; rpdid=|(RllRkY)kl0J'u~YJkYJ|~k; b_lsid=4651045D9_19A8AAC0A05; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; sid=8m05y3r0; CURRENT_FNVAL=2000; home_feed_column=4; browser_resolution=403-730"}

response = requests.get(url=bili_url,headers = headers)
print(response.encoding)#ISO-8859-1
response.encoding = 'utf-8'
print(response.text)
print(type(response.text))