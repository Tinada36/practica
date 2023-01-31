import requests
from bs4 import BeautifulSoup
import lxml


def torrlistblack(response, torrList,Class):
  soup = BeautifulSoup(response.text, 'lxml')
  torrlistBlack = soup.find_all('tr', class_=f"{Class}" )
  for i in range(len(torrlistBlack)):
    torrList.append([torrlistBlack[i].text.split('\n')[3], int(str(torrlistBlack[i]).split('download.php?id=')[1].split('"')[0])])


def main():

  proxies = {
  "https" : "socks5://user101021:kf2xdg@191.101.65.240:16400"
  }
  search = input("Введите запрос: ")
  
  s = requests.Session()
  username = input("Введите свой логин: ")
  password = input("Введите свой пароль: ")
  login_data = {'username': username, 'password': password, 'login': 'Вход'}
  response = s.post('https://nnmclub.to/forum/login.php', data=login_data,proxies=proxies)

  response = s.get(f'https://nnmclub.to/forum/tracker.php?nm={search}', proxies=proxies)
  torrList = []
  torrlistblack(response, torrList, 'prow1')
  torrlistblack(response, torrList, 'prow2')
  if len(torrList) == 0:
    print("Ничего не найдено")
    quit()
  num = int(input(f"Введите количесво результатов(до {len(torrList)}): "))
  for i in range(num):
    print(f'{i+1}. {torrList[i][0]}')
  choose = int(input('Выберите torrent: '))
  print(f'Скачивание {torrList[choose-1][0]}')

  r = s.get(f'https://nnmclub.to/forum/download.php?id={torrList[choose-1][1]}', proxies=proxies)
  open(f'{search}.torrent','wb').write(r.content)

  print('Успешно')


if __name__ == "__main__":
  main()