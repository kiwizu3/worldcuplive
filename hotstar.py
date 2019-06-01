import json
from datetime import date, timedelta
import datetime
import scrape

d1 = date(2019, 5, 30)  # start date
d2 = date(2019, 7, 14)  # end date
delta = d2 - d1         # timedelta

streaming_quality=['540p','720p','1080p']
double_match_numbers=[3,8,12,20,28,36,44]
double_match_dates=['06july2019','29june2019','22june2019','15june2019','08june2019','05june2019','01june2019']
clashing_matches={'01june2019':3,'05june2019':8,'08june2019':12,'15june2019':20,'22june2019':28,'29june2019':36,'06july2019':44}
match_dates=['30may2019', '31may2019', '01june2019', '02june2019', '03june2019', '04june2019', '05june2019', '06june2019', '07june2019', '08june2019', '09june2019', '10june2019',
'11june2019', '12june2019', '13june2019', '14june2019', '15june2019', '16june2019', '17june2019', '18june2019', '19june2019', '20june2019', '21june2019', '22june2019', '23june2019',
'24june2019', '25june2019', '26june2019', '27june2019', '28june2019', '29june2019', '30june2019', '01july2019', '02july2019', '03july2019', '04july2019', '05july2019', '06july2019', '09july2019',  '11july2019', '14july2019']

matchids={'30may2019': 1, '31may2019': 2, '01june2019': 3, '02june2019': 5, '03june2019': 6, '04june2019': 7, '05june2019': 8, '06june2019': 10, '07june2019': 11, '08june2019': 12, '09june2019': 14, '10june2019': 15, '11june2019': 16, '12june2019': 17, '13june2019': 18,
 '14june2019': 19, '15june2019': 20, '16june2019': 22, '17june2019': 23, '18june2019': 24, '19june2019': 25, '20june2019': 26, '21june2019': 27, '22june2019': 28, '23june2019': 30, '24june2019': 31, '25june2019': 32, '26june2019': 33, '27june2019':34, '28june2019': 35,
 '29june2019': 36, '30june2019': 38, '01july2019': 39, '02july2019': 40, '03july2019': 41, '04july2019': 42, '05july2019': 43, '06july2019': 44, '09july2019': 46, '11july2019': 47, '14july2019': 48}

def getMatchDetails(matchNumber):
    with open('wc19.json') as json_file:
        data = json.load(json_file)
        #print(data[str(matchNumber)])
        return (data[str(matchNumber)]['Match'])

def getDate():
    d1= date(2019, 5, 29)
    '''
    match_dates=[]
    for i in range(delta.days + 1):
        d1 += datetime.timedelta(days=1)
        match_dates.append(d1.strftime("%d%B%Y").lower())
    '''
    j=1
    for i in range(len(match_dates)):
        if match_dates[i] in double_match_dates:
            matchids[match_dates[i]]=j
            j=j+2
        else:
            matchids[match_dates[i]]=j
            j=j+1

    return matchids



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
    key=scrape.extract_code()
    try:
        if str(matchNumber)==str(key[0])[0:2]:
            hotstar_url=base_url+str(key[0])+date+'/'+trail;
        else:
            hotstar_url=base_url+str(key[1])+date+'/'+trail;
    except IndexError:
        return 'https://cyberboysumanjay.github.io/comingsoon.html'
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
#print(getDate())

def getMatchNumber(date):
    return matchids[date]
print(getMatchDetails(3))
