import re
import requests
def F(url,list_new,list_new1, url_new):
    r = requests.get(url_new)  #получает содержимое страницы    
    list = re.findall(r'[a-zA-Z0-9][-a-zA-Z0-9_.]*\@[-a-zA-Z]+\.[a-z]{2,6}',str(r.content)) #email
    for x in list:
        if x not in list_new:
           list_new.append(x)     
    list = re.finditer(r'(<a href=")(http\:\/\/[-+\w.\/$#%]+)(\")',str(r.content))  #http
    for x in list:
        if x.group(2).startswith(url) and (x.group(2) not in list_new1):
            list_new1.append(x.group(2))
    list = re.finditer(r'(<a href=")(\/[-+\w:\/#.&%$@]*)(\")', str(r.content))   #obrub http
    for x in list:
        url1=url+x.group(2)
        if url1 not in list_new1:
            list_new1.append(url1)
    return

url="http://www.mosigra.ru/"
rep_url=[]
rep_url.append(url)#список url
rep_email=[]
i=0
while i<10: #len(rep_url):
    url_new=str(rep_url[i])
    #print(url_new)
    F(url,rep_email,rep_url, url_new)
    i=i+1
print(rep_email)    

