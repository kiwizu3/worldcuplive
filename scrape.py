import re,requests,json
from bs4 import BeautifulSoup
from datetime import date

def get_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        np_list.append(i)
    #print(len(np_list))
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    print(len(proxy))
    return(proxy)

def extract_code():
    try:
        today = date.today()
        d = today.strftime("%d%B%Y").lower()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        proxies=get_proxy()
        for proxy in proxies:
            try:
                response=requests.get('https://saidit.net/user/DizzySphinzx',headers=headers,proxies={"http": proxy, "https": proxy}).text
                break
            except Exception:
                pass
        bsObj = BeautifulSoup(response,'html.parser');
        allLinks,hotstarLinks=[],[]
        for link in bsObj.find_all('a'):
            allLinks.append(link.get('href'))

        for link in allLinks:
            if 'hotstar' in str(link):
                if d in link:
                    hotstarLinks.append(link)

        key=[]
        for i in list(set(hotstarLinks)):
            i=i.split('fulldvrm')[1]
            i=i.split(d)[0]
            key.append(i)
        if len(key)>0:
            return(list(set(key)))
        raise AssertionError
    except Exception as e:
        print(e)
        return 'notavailable'

#print(extract_code())
