import requests
import fake_useragent
from bs4 import BeautifulSoup as pars

user =  fake_useragent.UserAgent().random
header = {
    'User-Agent': user
}
datas = {
    'login_username': 'def',
    'login_password': 'def'
}

login = input('Введите Логин: ')
passwd = input('Введите пароль: ')
search = input('Введите данные для поиска: ').split(' ')
search2 = int(input('Введите кол-во нужных результатов: '))
datas['login_username'] = login
datas['login_password'] = passwd
b = ''
for i in range(len(search)):
    if i == len(search)-1:
        b += search[i]
    else:
        b += search[i] + '%20'
    print(b)

URL = 'https://rutracker.org/forum/login.php'               # страница авторизации
s = requests.Session()
prof_info = f'https://rutracker.org/forum/search.php?nm={b}'        # страница с результатом поиска

s.headers.update({'User-Agent': user})
r = s.post(URL, {
     'login_username': login,
     'login_password': passwd,
     'login': 'pushed',
     'redirect': 'search.php'
})
res = s.get(prof_info, headers=header)
print(res.status_code)
soup = pars(res.text, 'html.parser')
href = []
for g in soup.findAll('a', class_="topictitle ts-text"):
    href.append(g.get('href'))
for i in range(search2):
    print(href[i])

change = input("Напишите название выбранной вами ссылки: ")

res = s.get(f'https://rutracker.org/forum/{change}', headers=header)
soup = pars(res.text, 'html.parser')
for i in soup.find_all('a', class_="dl-stub dl-link dl-topic"):
    links = i.get('href')
    print(links)

dnwl = input("Напишите название ссылки начинающейся на <<dl>>: ")

def donwlod_file(url=''):
    try:
        response = s.get(url=url, headers=header)
        with open('D:\File.torrent', 'wb') as f:
            f.write(response.content)
        return "All good"
    except Exception:
        return "Error!"

print(donwlod_file(url=f'https://rutracker.org/forum/{dnwl}'))