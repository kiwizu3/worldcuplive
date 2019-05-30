import json
from datetime import date, timedelta
import datetime

d1 = date(2019, 5, 30)  # start date
d2 = date(2019, 7, 14)  # end date
delta = d2 - d1         # timedelta


def getDate():
    d1= date(2019, 5, 29)
    match_dates=[]
    for i in range(delta.days + 1):
        d1 += datetime.timedelta(days=1)
        match_dates.append(d1.strftime("%d%B%Y").lower())
    return match_dates

streaming_quality=['540p','720p','1080p']
double_match_dates=['06july2019','29june2019','22june2019','15june2019','08june2019','05june2019','01june2019']
match_dates=(getDate())

def getLink(quality,language,date,matchNumber):
    base_url="https://live12.akt.hotstar-cdn.net/hls/live/2003704/icccwc2019/hin/15mindvrm"
    trail=""
    #today = date.today()
    #fixedDate = today.strftime("%d%B%Y").lower()
    if quality=="540p":
        trail="master_3.m3u8"
    elif quality=="720p":
        trail="master_4.m3u8"
    elif quality=="1080p":
        trail="master_5.m3u8"
    hotstar_url=base_url+str(matchNumber)+date+'/'+trail;
    if language.lower()=="english":
        hotstar_url=hotstar_url.replace("live12", "live11");
        hotstar_url=hotstar_url.replace("hin/", "eng/");
        hotstar_url=hotstar_url.replace("2003704","2003693");
    return hotstar_url

def linkJSON():
    languages=['hindi','english']
    master={}
    temp={}
    temp2={}
    d={}
    q,r={},{}

    for date in match_dates:

        if date in double_match_dates:
            for language in languages:
                for quality in streaming_quality:
                    q[quality]=getLink(quality,language,date,'01')
                    r[quality]=getLink(quality,language,date,'02')
                temp[language]=q
                temp2[language]=r
                q,r={},{}
            a=[]
            a.append(temp)
            a.append(temp2)
            d[date]=a
            temp={}
            temp2={}
        else:
            for language in languages:
                for quality in streaming_quality:
                    q[quality]=getLink(quality,language,date,'01')
                temp[language]=q
                q={}
            a=[]
            a.append(temp)
            d[date]=a
            temp={}
    master['links']=d
    with open('hotstar_links.json', 'w') as json_file:
        json.dump(master, json_file)

#linkJSON()
