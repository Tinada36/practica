from bs4 import BeautifulSoup
import requests
import time
from fake_useragent import UserAgent
import os
search = input("Введите ключевое слово для поиска проекта: ")
search2 = int(input("Введите кол-во результатов поиска: "))
print("""Выберите параметры сортировки:
1. Best match
2. Most stars
3. Fewest stars
4. Most forks
5. Fewest forks
6. Recently updated
7. Least recently updated""")
search3 = int(input(":"))
t = 1
s = requests.Session()
user = UserAgent().random
header = {
    'user-agent': user
}
if search3 == 1:
    url = f"https://github.com/search?o=desc&q={search}&s=&type=Repositories"
elif search3 == 2:
    url = f"https://github.com/search?o=desc&q={search}&s=stars&type=Repositories"
elif search3 == 3:
    url = f"https://github.com/search?o=asc&q={search}&s=stars&type=Repositories"       
elif search3 == 4:
    url = f"https://github.com/search?o=desc&q={search}&s=forks&type=Repositories"
elif search3 == 5:
    url = f"https://github.com/search?o=asc&q={search}&s=forks&type=Repositories"
elif search3 == 6:
    url = f"https://github.com/search?o=desc&q={search}&s=updated&type=Repositories"
elif search3 == 7:
    url = f"https://github.com/search?o=asc&q={search}&s=updated&type=Repositories"
r = s.get(url, headers=header)
time.sleep(t)
soup = BeautifulSoup(r.text, "html.parser")
languages = soup.find_all("a", class_="v-align-middle")
lst = [i.text for i in languages]
href = []
try:
    for i in range(search2):
        url_rep = f'https://github.com/{lst[i]}'
        r2 = s.get(url_rep, headers=header)
        print(r2.status_code)
        href.append(lst[i])
        time.sleep(t)
        soup1 = BeautifulSoup(r2.text, "html.parser")
        for g in soup1.find_all("span", class_="color-fg-default text-bold mr-1"):
            href.append(g.text)
        for k in soup1.find_all("a", title="README.md"):
            otv = 'https://github.com'
            href.append(otv + k.get('href'))
except IndexError:
    print("На странице меньше результатов чем вы запросили")
try:
    for i in range(len(href)):
        with open("pass_url.txt", "a+") as file:
            for g in range(len(lst)):
                if href[i] == lst[g]:
                    if str(href[i+1]).endswith("README.md") == True:
                        del href[i]
                        del href[i]
                        file.write("\nК сожалению не все результаты попали под фильтр интересующих репозиториев\n")
            if str(href[i]).endswith('README.md'):
                file.write(str(href[i])+'\n')
            else:
                file.write(f'{str(href[i])}, ')
except IndexError:
    pass

with open('pass_url.txt', 'r+') as f:
	line = f.readlines()
for i in range(len(line)):
    print(line[i])
os.remove("pass_url.txt")