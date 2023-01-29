import tkinter as tk
from tkinter import scrolledtext
import codecs
import time

def vopros():
  win.wm_resizable(0, 0)
  lbl.configure(text="Введите категорию теста")
  btn.configure(text="Принять", command=question)
  txt.place(x=120, y=200)
  lbl.place(x=220, y=180)
  btn.place(x=260, y=230)

def question():
  global line, b
  try:
    b = txt.get()
    fl = codecs.open(f"{b}_test.txt", "r+", "utf-8")
    txt.delete(0, tk.END)
    line = fl.read().replace("\r\n", "  ").split("  ")
    print(line)
    fl.close()
    zamena()
  except FileNotFoundError:
    lbl.configure(text="Такого теста ещё yt существует")

def zamena():
  lbl['text'] = line[i]
  btn.configure(command=check_var)
  txt.delete(0, tk.END)

def check_var():
  global chet, i
  a = txt.get()
  if a.lower() == line[i+1].lower():
    chet += 1
    txt.delete(0, tk.END)
    print(chet)
    if i + 2 == len(line)-1:
      end_test()
    else:
      i += 2
      zamena()
  else:
    txt.delete(0, tk.END)
    if i + 2 == len(line)-1:
      end_test()
    else:
      i += 2
      zamena()

def end_test():
  fl2 = codecs.open(f"{b}_test.txt", "r+", "utf-8")
  dlinna = fl2.readlines()
  fl2.close()
  fl = codecs.open("Results.txt", "a+", "utf-8")
  fl.write(f"{b}_test  {chet}/{len(dlinna)}\n")
  fl.close()
  lbl.configure(text=f"Ваш результат: {chet}/{len(dlinna)}")
  btn.configure(text="Завершить", command=zakritie)
  lbl.place(x=220, y=200)
  txt.place(x=10000, y=10000)
  btn.place(x=250, y=250)

def zakritie():
  win.destroy()

def admin():
  lbl.configure(text="Панель администратора")
  btn.configure(text="Добавить вопрос", command=add_vopros)
  btn1.configure(text="Создать тест", bg="#808080", command=create_test)
  txt.configure(width=50)
  btn2.configure(text="Просмотреть результаты", command=check_result)
  txt1.delete('1.0', tk.END)
  lbl.place(x=230, y=80)
  btn.place(x=245, y=150)
  btn1.place(x=255, y=200)
  btn2.place(x=225, y=250)
  txt.place(x=10000, y=10000)
  txt1.place(x=10000, y=10000)

def add_vopros():
  lbl.configure(text="Напишите название теста, куда вы хотите добавить вопрос")
  btn.configure(text="Принять", command=open_test)
  btn1.configure(text="Назад", command=admin)
  lbl.place(x=122, y=150)
  txt.place(x=120, y=200)
  btn.place(x=260, y=250)
  btn1.place(x=0, y=0)
  btn2.place(x=10000, y=10000)

def open_test():
  global f
  a = txt.get()
  f = codecs.open(f'{a}_test.txt', 'a+', 'utf-8')
  txt.delete(0, tk.END)
  lbl.configure(text="Напишите вопрос и через 2 пробела ответ")
  btn.configure(text="Принять", command=write_question)
  lbl.place(x=225, y=150)

def write_question():
  a = txt.get()
  f.write(a + "\n")
  f.close()
  txt.delete(0, tk.END)
  admin()

def create_test():
  lbl.configure(text="Придумайте название теста")
  btn1.configure(text="Назад", command=admin)
  btn.configure(text="Принять", command=open_test)
  lbl.place(x=190, y=150)
  txt.place(x=120, y=200)
  btn.place(x=260, y=250)
  btn1.place(x=0, y=0)
  btn2.place(x=10000, y=10000)

def check_result():
  btn1.configure(text="Назад", command=admin)
  txt.configure(width=40)
  fil = codecs.open("Results.txt", "r+", "utf-8")
  line = fil.read()
  txt1.insert('1.0', line)
  lbl.configure(text="Введите тест для поиска результата")
  btn.configure(text="Поиск", command=search)
  lbl.place(x=180, y=50)
  txt.place(x=120, y=70)
  btn.place(x=410, y=69)
  btn1.place(x=0, y=0)
  btn2.place(x=10000, y=10000)
  txt1.place(x=100, y=110)

def search():
  a = txt.get()
  txt1.delete('1.0', tk.END)
  fil = codecs.open("Results.txt", "r+", "utf-8")
  liness = fil.read().replace("\n", "  ").split("  ")
  print(liness)
  for i in range(len(liness)):
    if a == liness[i]:
      txt1.insert('1.0', f'{liness[i]}: {liness[i+1]}\n')
  txt.delete(0, tk.END)

win = tk.Tk()
chet = 0
i = 0
win.title("Квиз-тест")
win.geometry('600x400')
win['bg'] = "#CD5C5C"
lbl = tk.Label(win, font=('arial',9,'bold'), bg='#CD5C5C')
lbl1 = tk.Label(win, font=('arial',9,'bold'), bg='#CD5C5C')
txt = tk.Entry(win, width=50, justify="center", font=('arial',9,'bold'))
txt1 = scrolledtext.ScrolledText(win, height=17, width=55, fg='#0000FF', font=('arial',9,'bold'))
btn = tk.Button(win, text="Начать", bg='#808080', fg="#FFFF00", font=('arial',9,'bold'), command=vopros)
btn1 = tk.Button(win, bg='#CD5C5C', fg="#FFFF00", font=('arial',9,'bold'), command=admin)
btn2 = tk.Button(win, bg='#808080', fg="#FFFF00", font=('arial',9,'bold'))
btn.place(x=260, y=150)
btn1.place(x=1000, y=760)
win.mainloop()