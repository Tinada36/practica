import tkinter as tk
from tkinter import scrolledtext
import codecs

with codecs.open('zametki\data.txt', 'r+', 'utf-8') as f:
    ln = f.readline()
    lst = ln.split(', ')

print(lst)

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
            with codecs.open(f'{poluch}_polz.txt', 'w+', 'utf-8') as file1:
                file1.write("Заметки:\n")
            with codecs.open('zametki\data.txt', 'a+', 'utf-8') as ff:
                ff.write(str(f', {poluch}'))
            client()
            break

def client():
    lbl.configure(text="Введите новую заметку")
    btn.configure(text='Принять', command=messange)
    txt.delete(0, tk.END)
    txt.configure(width=50)
    with codecs.open(f"{poluch}_polz.txt", "r+", "utf-8") as file:
        line = file.read()
        txt1.insert('1.0', line)
    txt.place(x=115, y=90) 
    btn.place(x=260, y=120)
    txt1.place(x=110, y=160)
    lbl.place(x=220, y=50)

def messange():
    zametka = txt.get()
    txt.delete(0, tk.END)
    with codecs.open(f"{poluch}_polz.txt", "a+", "utf-8") as file:
        file.write(f"{zametka}\n")
        txt1.insert(tk.END, f"{zametka}\n")

win = tk.Tk()
win.title("ZAMETKI")
win.geometry('600x400')
win['bg'] = "#F0E68C"
win.wm_resizable(0, 0)
lbl = tk.Label(win, text="Введите имя",bg="#F0E68C", font=('arial',9,'bold'))
txt = tk.Entry(win, width=10, justify="center", font=('arial',9,'bold'))
txt1 = scrolledtext.ScrolledText(win, height=12, width=50, fg='#A52A2A', font=('arial',9,'bold'))
btn = tk.Button(win, text="Принять", command=zapros, bg="#4B0082", fg="#FFC0CB", font=('arial',9,'bold'))
btn.place(x=260, y=160)
txt.place(x=260, y=130)
lbl.place(x=255, y=110)
win.mainloop()