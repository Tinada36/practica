# система хранения ссылок

# ссылки и пароли к ним сохраняются в один файл
import pyautogui as pya
import pyperclip
import codecs
import time
import re

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()

def search(name):
    with codecs.open("base_url.txt", "r+", "utf-8") as f:
        line = f.readlines()
        for i in range(len(line)):
            if re.search(name, str(line[i])):
                print(line[i])
                break
            elif i == len(line)-1:
                print("Такой ссылки нет :(")

def copy_text():
    copy = int(input("Если хотите автокопировать ссылку введите 1 и наведите на неё курсор, если нет любую другую: "))

    if copy == 1:
        time.sleep(1)
        pya.doubleClick(pya.position())
        lst = []
        var = copy_clipboard()
        lst.append(var) 
        print("Ссылка скопирована в буфер обмена")
    else:
        print("Всего хорошего!")

print("""Вас приветствует система хранения ссылок.
Если хотите сохранить ссылку нажмите 1.
Если хотите найти имеющуюся ссылку нажмите 2.
Если хотите выйти нажмите любую другую цифру.""")
try:
    change = int(input(":"))
except ValueError:
    print("Вы ввели не цифру")
    exit()


if change == 1:
    person = input('Введите ссылку, которую необходима сохранить: ')
    check = int(input('Если есть пароль от сайта введите 1, если нет 2: '))
    if check == 1:
        pswd = input('Введите пароль: ')
        with codecs.open('base_url.txt', 'a+', 'utf-8') as file:
            file.write(str(person) + "     пароль: " + str(pswd) + "\n")
    else:
        with codecs.open('base_url.txt', 'a+', 'utf-8') as file:
            file.write(str(person) + "\n")
    copy_text()
elif change == 2:
    name_url = input("Введите ключевое слово для поиска названия ссылки: ")
    search(name_url)
    copy_text()
else:
    print("Досвидания!")