from django.shortcuts import render
from django.http import JsonResponse
from project1.twe import getTweet
import json

tweet = getTweet()


def myView(request):

    resp = {
        "latitude": tweet.decode['coordinates']['coordinates'][1],
        "longitude": tweet.decode['coordinates']['coordinates'][0],
        "nlpKey": int(tweet.decode['nlpKey']),
        "nbKey": int(tweet.decode['nbKey']),
        "id": tweet.decode['id'],
        "name": tweet.decode['user']['name'],
        "text": tweet.decode['text'],
        
        
        "pic": tweet.decode['user']['profile_image_url'],
        "date": tweet.decode['created_at']
    }
    print(tweet.decode['nbKey'],'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkkhkhkhlkgfdfgyhuijhvcf')
    print(tweet.decode['nbKey'],'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkkhkhkhlkgfdfgyhuijhvcf')
    print(tweet.decode['nbKey'],'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkkhkhkhlkgfdfgyhuijhvcf')
    return JsonResponse(resp, safe=False)



"""resp = {
    "id": tweet.decode['id'],
    "name": tweet.decode['user']['name'],
    "text": tweet.decode['text'],
    "fillKey1": tweet.decode['fillKey1'],
    {"id":1114600622756638700,"name":"خـــلود🕊 #تطوع","text":"انا ما قلت شي اصلا انا ما ربيعة حد🙂💔","fillKey1":1,"fillKey":0,"latitude":null,"longitude":null,"pic":{"id":3241743440,"id_str":"3241743440","name":"خـــلود🕊 #تطوع","screen_name":"kholoodalyasi","location":"Sohar, Oman","url":"https://www.instagram.com/kholood_alyasi/","description":"#مهندسة مدنية(CE)⛑ #مدربة معتمدة من الأكاديمية البريطانية(GATD) #الرخصة التطوعية🔖رئيسة لجنة العلاقات ب#اليراع واللجنة التنظيمية ب#رابطة تأثير🔗 #متطوعه♻️","translator_type":"none","protected":false,"verified":false,"followers_count":1453,"friends_count":2441,"listed_count":6,"favourites_count":6445,"statuses_count":12385,"created_at":"Wed Jun 10 22:53:48 +0000 2015","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","profile_background_image_url_https":"https://abs.twimg.com/images/themes/theme1/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http://pbs.twimg.com/profile_images/1110026852289122304/YGcbx5nz_normal.jpg","profile_image_url_https":"https://pbs.twimg.com/profile_images/1110026852289122304/YGcbx5nz_normal.jpg","profile_banner_url":"https://pbs.twimg.com/profile_banners/3241743440/1551882356","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"date":"Sat Apr 06 18:47:51 +0000 2019"}	
00:18:36.844
message	{"id":1114600625730355200,"name":"Aizen.","text":"Just wanna get high and enjoy the rain","fillKey1":1,"fillKey":0,"latitude":null,"longitude":null,"pic":{"id":348861739,"id_str":"348861739","name":"Aizen.","screen_name":"clew142","location":"Killeen, TX","url":null,"description":"#LCCJ #RetiredHooper 👻: cleww142","translator_type":"none","protected":false,"verified":false,"followers_count":1096,"friends_count":952,"listed_count":9,"favourites_count":53737,"statuses_count":69503,"created_at":"Fri Aug 05 03:44:58 +0000 2011","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png","profile_background_image_url_https":"https://abs.twimg.com/images/themes/theme1/bg.png","profile_background_tile":true,"profile_link_color":"B30000","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"000000","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http://pbs.twimg.com/profile_images/1097611651707228161/H6SFarga_normal.jpg","profile_image_url_https":"https://pbs.twimg.com/profile_images/1097611651707228161/H6SFarga_normal.jpg","profile_banner_url":"https://pbs.twimg.com/profile_banners/348861739/1537334674","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"date":"Sat Apr 06 18:47:52 +0000 2019"}	

    "fillKey": 0,
    "latitude": tweet.decode['coordinates'],
    "longitude": tweet.decode['coordinates'],
    "pic": tweet.decode['user'],
    "date": tweet.decode['created_at']
}
resp = {working
        "id": tweet.decode['id'],
        "name": tweet.decode['user']['name'],
        "text": tweet.decode['text'],
        "fillKey1": 0,
        "fillKey": 0,
        "latitude": tweet.decode['coordinates'],
        "longitude": tweet.decode['coordinates'],
        "pic": tweet.decode['user']['profile_image_url'],
        "date": tweet.decode['created_at']
    }"""
