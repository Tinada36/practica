import datetime
import tkinter as tk
from tkinter import scrolledtext
import codecs

with codecs.open('data.txt', 'r+', 'utf-8') as f:
    ln = f.readline()
    lst = ln.split(', ')

print(lst)

def pincode():
    txt.place(x=260, y=130)
    btn.configure(text="Войти", command=zapros)
    lbl.configure(text="Введите имя")
    btn.place(x=262, y=160)
    lbl.place(x=260, y=110)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)


def zapros():
    global poluch
    poluch = txt.get()
    print(poluch)
    for i in range(len(lst)):
        if poluch == lst[i]:
            client()
            break
        elif i == len(lst)-1:
            print('HERE')
            client()
            with codecs.open(f'{poluch}_balans.txt', 'w+', 'utf-8') as file1:
                file1.write(str(f'Balans: {balans}'))
            with codecs.open('data.txt', 'a+', 'utf-8') as ff:
                ff.write(str(f', {poluch}'))
            break

def client():
    btn.configure(text='Положить сумму', command=deposit_money)
    btn1.configure(text='Забрать сумму', command=cash_get)
    btn2.configure(text='Завершить операцию', command=end_operations)
    btn3.configure(text='Проверить баланс', command=check_balans)
    btn4.configure(text='Вложить под %', command=procent)
    txt1.delete('1.0', tk.END)

    btn.place(x=225, y=140)
    btn1.place(x=225, y=180)
    btn2.place(x=225, y=260)
    btn3.place(x=225, y=100)
    btn4.place(x=225, y=220)
    txt.place(x=10000, y=10000)
    txt_ent.place(x=10000, y=10000)
    txt_ent1.place(x=10000, y=10000)
    txt_ent2.place(x=100000, y=100000)
    txt1.place(x=100000, y=10000)
    lbl.place(x=10000, y=10000)

def check_balans():
    txt1.place(x=100, y=75)
    btn.configure(text='Назад', command=client)
    btn.place(x=10, y=10)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)
    with codecs.open(f'{poluch}_balans.txt', 'r+', 'utf-8') as file:
        line = file.read()
        txt1.insert('1.0', line)
    try:
        with codecs.open(f'{poluch}_procent.txt', 'r+', 'utf-8') as f:
            line1 = f.read()
            txt1.insert('1.0', line1)
    except FileNotFoundError:
        pass

def deposit_money():
    lbl.configure(text="Введите сумму для пополнения: ")
    txt_ent.place(x=255, y=150)
    btn.configure(text="Пополнить", command=sum_balans)
    lbl.place(x=210, y=130)
    btn.place(x=250, y=180)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)
    txt_ent1.place(x=100000, y=100000)
    txt_ent2.place(x=100000, y=100000)
    txt.place(x=100000, y=100000)

def sum_balans():
    global balans
    vvod = txt_ent.get()
    balans = int(balans) + int(vvod)
    lbl.configure(text="Готово!")
    lbl.place(x=260, y=130)
    btn.configure(text="Вернуться", command=client)
    txt_ent1.place(x=100000, y=100000)
    txt.place(x=100000, y=100000)
    txt_ent.place(x=100000, y=100000)
    txt_ent2.place(x=100000, y=100000)
    print(balans)
    with codecs.open(f'{poluch}_balans.txt', 'w+', 'utf-8') as file:
        file.write(str(f'Balans: {balans}'))

def cash_get():
    lbl.configure(text="Введите сумму для снятия: ")
    txt_ent1.place(x=250, y=160)
    btn.configure(text="Снять", command=check)
    lbl.place(x=210, y=130)
    btn.place(x=260, y=190)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)
    txt_ent.place(x=1000000, y=1000000)
    txt_ent2.place(x=100000, y=100000)
    txt.place(x=100000, y=100000)

def check():
    global balans
    vivod = txt_ent1.get()
    ff = codecs.open(f'{poluch}_balans.txt', 'r+')
    a = ff.readline()
    l = a.split(" ")
    ff.close()
    balans = int(l[1])
    if int(balans) >= int(vivod):
        balans = int(balans) - int(vivod)
        lbl.configure(text="Готово!")
        btn.configure(text="Назад", command=client)
        with codecs.open(f'{poluch}_balans.txt', 'w+', 'utf-8') as file:
            file.write(str(f'Balans: {balans}'))
        lbl.place(x=260, y=150)
        btn.place(x=260, y=170)
        btn1.place(x=1000000, y=1000000)
        btn3.place(x=1000000, y=1000000)
        btn2.place(x=1000000, y=1000000)
        btn4.place(x=1000000, y=1000000)
        txt_ent.place(x=1000000, y=1000000)
        txt_ent1.place(x=100000, y=100000)
        txt_ent2.place(x=100000, y=100000)
        txt.place(x=100000, y=100000)

    else:
        lbl.configure(text="У вас недостаточно средств.")
        btn.configure(text="Назад", command=client)
        lbl.place(x=260, y=150)
        btn.place(x=260, y=170)
        btn1.place(x=1000000, y=1000000)
        btn3.place(x=1000000, y=1000000)
        btn2.place(x=1000000, y=1000000)
        btn4.place(x=1000000, y=1000000)
        txt_ent.place(x=1000000, y=1000000)
        txt_ent1.place(x=100000, y=100000)
        txt_ent2.place(x=100000, y=100000)
        txt.place(x=100000, y=100000)

def procent():
    lbl.configure(text="Введите сумму для вложения под 50% на 100 дней: ")
    txt_ent2.place(x=255, y=150)
    btn.configure(text="Пополнить", command=vlozhenie)
    lbl.place(x=210, y=130)
    btn.place(x=250, y=180)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)
    txt_ent1.place(x=100000, y=100000)
    txt.place(x=100000, y=100000)

def vlozhenie():
    a = txt_ent2.get()
    local_time = datetime.date.today()
    with codecs.open(f'{poluch}_procent.txt', 'a+', 'utf-8') as ff:
        ff.write(str(f'\nСумма под процентом 50% на 100 дней: {a} с {local_time.strftime("%m/%d/%Y")}\n'))
    b = local_time.day + 100
    if local_time == b:
        a = a*0,5
        global balans
        fff = codecs.open(f'{poluch}_balans.txt', 'r+')
        a = fff.readline()
        l = a.split(" ")
        fff.close()
        balans = int(l[1]) + a
        with codecs.open(f'{poluch}_balans.txt', 'w+', 'utf-8') as ffff:
            ffff.write(str(f'Balans: {balans}'))
    lbl.configure(text="Готово!")
    btn.configure(text="Назад", command=client)
    lbl.place(x=250, y=130)
    btn.place(x=250, y=180)
    btn1.place(x=1000000, y=1000000)
    btn2.place(x=1000000, y=1000000)
    btn3.place(x=1000000, y=1000000)
    btn4.place(x=1000000, y=1000000)
    txt_ent1.place(x=100000, y=100000)
    txt_ent2.place(x=100000, y=100000)
    txt.place(x=100000, y=100000)
    

def end_operations():
    win.destroy()

win = tk.Tk()
win.title("KOPILKA")
win.geometry('600x400')
win.wm_resizable(0, 0)
balans = 0
lbl = tk.Label(win)
lbl1 = tk.Label(win)
txt = tk.Entry(win, width=10, justify="center")
txt_ent = tk.Entry(win, width=10, justify="center")
txt_ent1 = tk.Entry(win, width=10, justify="center")
txt_ent2 = tk.Entry(win, width=10, justify="center")
txt1 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
txt2 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
txt3 = scrolledtext.ScrolledText(win, height=15, width=50, fg='#0000FF')
btn = tk.Button(win, text="Начать", command=pincode)
btn1 = tk.Button(win)
btn2 = tk.Button(win)
btn3 = tk.Button(win)
btn4 = tk.Button(win)
btn.place(x=260, y=150)
win.mainloop()