import requests
url = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/69/33483196901/33483196901-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&nbs=1&platform=pc&trid=d096e3bff3414cdd95928d730e0d816u&gen=playurlv3&os=cosbv&og=cos&uipk=5&oi=455426825&deadline=1763353739&mid=3494358359738725&upsig=95f9cbb34e79a0fa325be7d7cb4066f6&uparams=e,nbs,platform,trid,gen,os,og,uipk,oi,deadline,mid&bvc=vod&nettype=0&bw=3002778&build=0&dl=0&f=u_0_0&agrr=0&buvid=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc&np=151371867&orderid=1,3", "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/69/33483196901/33483196901-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&mid=3494358359738725&uipk=5&oi=455426825&os=cosbv&nbs=1&trid=d096e3bff3414cdd95928d730e0d816u&deadline=1763353739&gen=playurlv3&og=cos&upsig=08ffbab93344068f80aa71a747aae26f&uparams=e,platform,mid,uipk,oi,os,nbs,trid,deadline,gen,og&bvc=vod&nettype=0&bw=3002778&np=151371867&build=0&dl=0&f=u_0_0&agrr=0&buvid=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc&orderid=2,3'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
'cookie':"buvid3=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc; b_nut=1763263021; _uuid=5D96A149-2918-10862-2726-A104AEC9D6141021728infoc; buvid4=7070262B-D05B-3887-524D-1E8A23B23A1822240-025111611-sSA5PGJPu868bv+N1mqzCQ%3D%3D; buvid_fp=df0d40d01dc665444357cbfb49fc7af7; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjM1MjIyMjIsImlhdCI6MTc2MzI2Mjk2MiwicGx0IjotMX0.g_5mNuzgWYYHUOgJhLJW-ihm7D-_oVKmbCk0PU-oLPo; bili_ticket_expires=1763522162; CURRENT_QUALITY=0; rpdid=|(RllRkY)kl0J'u~YJkYJ|~k; home_feed_column=5; browser_resolution=1536-730; b_lsid=434F1047A_19A8F76CE54; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; SESSDATA=c03a64a1%2C1778895547%2Cb6305%2Ab2; bili_jct=d2d7e2c2aabc1f67209b956f1fd694e3; DedeUserID=3494358359738725; DedeUserID__ckMd5=80e6252eb614dfb6; sid=6ti6a6jc; theme-tip-show=SHOWED; CURRENT_FNVAL=4048",
'referer':'https://www.bilibili.com/'

}
response = requests.get(url=url,headers=headers)
print(response.status_code)
print(response.content)
with open ('一拳超人.mp4','wb')as f:
   f.write(response.content)


audio_url='https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/69/33483196901/33483196901-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&trid=d096e3bff3414cdd95928d730e0d816u&uipk=5&os=cosbv&nbs=1&platform=pc&mid=3494358359738725&oi=455426825&deadline=1763353739&gen=playurlv3&og=cos&upsig=cc245d0d92f6367d08ece0ba213a49e0&uparams=e,trid,uipk,os,nbs,platform,mid,oi,deadline,gen,og&bvc=vod&nettype=0&bw=79605&dl=0&f=u_0_0&agrr=0&buvid=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc&np=151371867&build=0&orderid=1,3", "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/69/33483196901/33483196901-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&gen=playurlv3&uipk=5&mid=3494358359738725&os=cosbv&og=cos&oi=455426825&deadline=1763353739&nbs=1&platform=pc&trid=d096e3bff3414cdd95928d730e0d816u&upsig=4684830965b7a2770cb09b884342157b&uparams=e,gen,uipk,mid,os,og,oi,deadline,nbs,platform,trid&bvc=vod&nettype=0&bw=79605&buvid=323DB33A-AB70-29A8-6E38-1FF542BC24CB21629infoc&np=151371867&build=0&dl=0&f=u_0_0&agrr=0&orderid=2,3'
audio_response = requests.get(url=audio_url,headers = headers)
print(audio_response.content)
with open('一拳超人.mp3','wb')as f:
    f.write(audio_response.content)

