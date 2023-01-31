#http://202.5.221.66:60279/en/

import requests
import fake_useragent
from bs4 import BeautifulSoup as pars
import time
user =  fake_useragent.UserAgent().random
header = {
    'user-agent': user
}
datas = {
    'login': 'def',
    'password': 'def'
}

t = 1
login = input('Введите Логин: ')
passwd = input('Введите пароль: ')
search = input('Введите данные для поиска: ').split(' ')
search2 = int(input('Введите кол-во нужных результатов: '))
datas['login'] = login
datas['password'] = passwd
b = ''
for i in range(len(search)):
    if i == len(search)-1:
        b += search[i]
    else:
        b += search[i] + '%20'
    print(b)


URL = 'https://nnmclub.to/forum/login.php'               # страница авторизации
s = requests.Session()
loging = s.post(URL, data=datas, headers=header)
time.sleep(t)
prof_info = f'https://nnmclub.to/forum/tracker.php?nm={b}'         # страница с результатом поиска
prof_resp = s.get(prof_info, headers=header)
print(prof_resp.status_code)
time.sleep(t)

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}  
    for key in s.cookies
]
s2 = requests.Session()
for cookies in cookies_dict:
    s2.cookies.set(**cookies)

res = s2.get(prof_info, headers=header)
res.encoding = 'utf8'
time.sleep(t)
soup = pars(res.text, 'html.parser')
href = []
for g in soup.find_all('a', class_='genmed topictitle'):
    href.append(g.get('href'))
for i in range(search2):
    print(href[i])

change = input("Напишите название выбранной вами ссылки: ")

res = s2.get(f'https://nnmclub.to/forum/{change}', headers=header)
time.sleep(t)
soup = pars(res.text, 'html.parser')
aa = soup.select('span.genmed')
for i in aa:
    links = i.select('a')
    print(links)

dnwl = input("Напишите название ссылки начинающейся на <<donwload>>: ")

def donwlod_file(url=''):
    try:
        response = s2.get(url=url, headers=header)
        with open('D:\File.torrent', 'wb') as f:
            f.write(response.content)
        return "All good"
    except Exception:
        return "Error!"

print(donwlod_file(url=f'https://nnmclub.to/forum/{dnwl}'))