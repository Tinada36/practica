#gruzin_apelsin
#Tinada36

import requests
import fake_useragent
from bs4 import BeautifulSoup as pars
import tkinter as tk
from tkinter import scrolledtext

user =  fake_useragent.UserAgent().random
header = {
    'User-Agent': user
}
datas = {
    'login_username': 'def',
    'login_password': 'def'
}
def get_list():
    global s, change, scr, ent, btn, lbl
    login = entry1.get()
    passwd = entry2.get()
    search = entry3.get().split(' ')
    search2 = entry4.get()
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

    win = tk.Tk()
    win.geometry("600x400")
    ent = tk.Entry(win, width=30)
    ent.grid(row=1, column=0)
    btn = tk.Button(win, text="Get", command=vibor)
    btn.grid(row=1, column=1)
    lbl = tk.Label(win, text="Выберите название ссылки:")
    lbl.grid(row=0, column=0)
    scr = scrolledtext.ScrolledText(win, height=10, width=30)
    scr.grid(row=2, column=0)
    for i in range(int(search2)):
        scr.insert("1.0", href[i] + "\n")
    win.mainloop()
def vibor():
    change = ent.get()
    res = s.get(f'https://rutracker.org/forum/{change}', headers=header)
    soup = pars(res.text, 'html.parser')
    for i in soup.find_all('a', class_="dl-stub dl-link dl-topic"):
        links = i.get('href')
    scr.insert("1.0", links + "\n")
    lbl.configure(text="Напишите название ссылки начинающейся на <<dl>>: ")
    ent.delete(0, tk.END)
    btn.configure(command=donwlod_file)

def donwlod_file():
    dnwl = ent.get()
    try:
        response = s.get(url=f"https://rutracker.org/forum/{dnwl}", headers=header)
        with open('D:\File.torrent', 'wb') as f:
            f.write(response.content)
        print("All good")
    except Exception:
        print("Error!")

#print(donwlod_file(url=f'https://rutracker.org/forum/{dnwl}'))
root = tk.Tk()
root.title("Github")

root.configure(background='yellow')
root.geometry("600x300")


label1 = tk.Label(root, text="Введите Логин:", background='yellow')
label2 = tk.Label(root, text="Введите Пароль:", background='yellow')
label3 = tk.Label(root, text="Введите данные для поиска:", background='yellow')
label4 = tk.Label(root, text="Введите кол-во нужных результатов:", background='yellow')
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)


button = tk.Button(root, text="Get", command=get_list)
button.grid(row=1, column=2, columnspan=3, pady=10)

output_label = tk.Label(root, text="")
output_label.grid(row=4, column=0, columnspan=3)

root.mainloop()