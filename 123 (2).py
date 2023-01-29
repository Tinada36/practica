from datetime import datetime, date, time, timedelta
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import codecs


def enter_first_data():
    global d
    a = en.get()
    b = en2.get()
    c = en3.get()
    d = date(year=int(a), month=int(b), day=int(c))
    current_dates.append(d)
    en.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    lbl.configure(text="Введите дату окончания события")
    btn.configure(command=enter_last_data)
    lbl.place(x=300, y=150)

def enter_last_data():
    global date_date
    global date_date1
    a = en.get()
    b = en2.get()
    c = en3.get()
    d1 = date(year=int(a), month=int(b), day=int(c))
    date_date = d.strftime('%d/%m/%Y')
    date_date1 = d1.strftime('%d/%m/%Y')
    en.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    lbl.configure(text="Введите событие")
    lbl2.configure(text=" ")
    btn.configure(command=eventss)
    en.configure(width=50)
    lbl.place(x=350, y=150)
    btn.place(x=370, y=250)
    en.place(x=230, y=200)
    en2.place(x=100000, y=10000)
    en3.place(x=100000, y=10000)

def eventss():
    global event
    event = en.get()
    events.append(event)
    en.delete(0, END)
    lbl.configure(text="Нужно ли обозначить время для напоминания?")
    lbl2.configure(text="Введите y/n")
    en.configure(width=10)
    btn.configure(command=change)
    en.place(x=342, y=200)
    btn.place(x=350, y=250)
    lbl.place(x=255, y=150)

def yes():
    global date_time
    a = en.get()
    b = en2.get() 
    t = time(hour=int(a), minute=int(b))
    current_times.append(t)
    date_time = t.strftime('%H:%M:%S')
    en.delete(0, END)
    en2.delete(0, END)
    lbl.configure(text="Укажите время окончания")
    btn.configure(command=yes_2)


def yes_2():
    global date_time1
    a = en.get()
    b = en2.get() 
    t1 = time(hour=int(a), minute=int(b))
    current_times.append(t1)
    date_time1 = t1.strftime('%H:%M:%S')
    en.delete(0, END)
    en2.delete(0, END)
    write_data()
    lbl.configure(text="Хотите добавить заметку для события?")
    lbl2.configure(text="Введите y/n")
    en.configure(width=10)
    btn.configure(command=zametka)
    en.place(x=342, y=200)
    en2.place(x=100000, y=100000)
    btn.place(x=350, y=250)
    lbl.place(x=265, y=150)

def write_data():
    f = codecs.open('logs.txt', 'a', 'utf-8')
    f.write('Событие ' + event)
    f.write(' ')
    f.write('Начало: ' + date_date)
    f.write(' ')
    f.write('Конец: ' + date_date1)
    f.write(' ')
    f.write('Время начала: ' + date_time)
    f.write(' ')
    f.write('Время окончания: ' + date_time1)
    f.write('\n')
    print('logs.txt completed, pls check file')

def change():
    time_flag = en.get()
    en.delete(0, END)
    if time_flag == 'y':
        lbl.configure(text="Укажите время начала")
        lbl2.configure(text="часы и минуты")
        lbl.place(x=330, y=150)
        en.place(x=300, y=200)
        en2.place(x=400, y=200)      
        btn.configure(command=yes)     
    else:
        lbl.configure(text="Хотите добавить заметку для события?")
        lbl2.configure(text="Введите y/n")
        en.configure(width=10)
        btn.configure(command=zametka)
        en.place(x=342, y=200)
        en2.place(x=100000, y=100000)
        btn.place(x=350, y=250)
        lbl.place(x=265, y=150)

def add_zametka():
    a = en.get()
    notes.append(a)
    en.delete(0, END)
    lbl.configure(text='Хотите добавить место события?')
    lbl2.configure(text='Введите y/n')
    en.configure(width=10)
    btn.configure(command=mesto)
    en.place(x=342, y=200)
    btn.place(x=350, y=250)
    lbl.place(x=275, y=150)


def zametka():
    notes_flag = en.get()
    en.delete(0, END)
    if notes_flag == 'y':
        lbl.configure(text='Введите заметку')
        lbl2.configure(text=" ")
        en.configure(width=50)
        btn.configure(command=add_zametka)
        lbl.place(x=350, y=150)
        btn.place(x=370, y=250)
        en.place(x=230, y=200)
    else:
        notes.append('Для данного события нет заметки')
        lbl.configure(text='Хотите добавить место события?')
        lbl2.configure(text='Введите y/n')
        en.configure(width=10)
        btn.configure(command=mesto)
        en.place(x=342, y=200)
        btn.place(x=350, y=250)
        lbl.place(x=275, y=150)

def add_url():
    a = en.get()
    place.append(a)
    en.delete(0, END)
    lbl.configure(text='Хотите добавить email учавствующих?')
    lbl2.configure(text='Введите y/n')
    en.configure(width=10)
    btn.configure(command=emaill)
    en.place(x=342, y=200)
    btn.place(x=350, y=250)
    lbl.place(x=265, y=150)

def mesto():
    place_flag = en.get()
    en.delete(0, END)
    if place_flag == 'y':
        lbl.configure(text='Введите ссылку на место')
        lbl2.configure(text=" ")
        en.configure(width=50)
        btn.configure(command=add_url)
        lbl.place(x=350, y=150)
        btn.place(x=370, y=250)
        en.place(x=230, y=200)
    else:
        place.append('Для данного события нет места')
        lbl.configure(text='Хотите добавить email учавствующих?')
        lbl2.configure(text='Введите y/n')
        en.configure(width=10)
        btn.configure(command=emaill)
        en.place(x=342, y=200)
        btn.place(x=350, y=250)
        lbl.place(x=265, y=150)

def add_email():
    a = en.get()
    email.append(a)
    en.delete(0, END)
    lbl.configure(text='Для просмотра нажмите кнопку')
    lbl2.configure(text=' ')
    btn.configure(text="Нажать", command=pokaz)
    en.place(x=100000, y=100000)
    btn.place(x=350, y=250)
    lbl.place(x=285, y=150)

def emaill():
    email_flag = en.get()
    en.delete(0, END)
    if email_flag == 'y':
        lbl.configure(text='Введите емейлы через пробел')
        lbl2.configure(text=" ")
        en.configure(width=50)
        btn.configure(command=add_email)
        lbl.place(x=335, y=150)
        btn.place(x=370, y=250)
        en.place(x=230, y=200)
    else:
        email.append('Для данного события нет емейлов')
        lbl.configure(text='Для просмотра нажмите кнопку')
        lbl2.configure(text=' ')
        btn.configure(text="Нажать", command=pokaz)
        en.place(x=100000, y=100000)
        btn.place(x=350, y=250)
        lbl.place(x=285, y=150)

def pokaz():
    txt = scrolledtext.ScrolledText(root, height=30, width=80, bg="#7FFFD4")
    txt.place(x=80, y=75)
    with codecs.open("logs.txt", "r+", "utf-8") as f:
        line = f.read()
        txt.insert("1.0", line)
    for i in notes:
        txt.insert(END, f"Заметка {i}\n")
    for i in place:
        txt.insert(END, f"Место {i}\n")
    for i in email:
        txt.insert(END, f"Email {i}\n")
    check_event_time()
    clear_file()
    

def check_event_time():
    for i in range(len(current_dates)):
        if datetime.now().date() == current_dates[i]:
            messagebox.showinfo('Text', f'Событие {events[i]} уже сегодня!')
            warning = timedelta(minutes=5)
            while True:
                x = datetime.now().time()
                x = timedelta(hours=x.hour, minutes=x.minute)
                y = timedelta(hours=current_times[i].hour, minutes=current_times[i].minute)
                if x + warning == y:
                    messagebox.showinfo('Text', 'До события осталось 5 минут, поторпитесь')
                    break

def clear_file():
    try:
        with codecs.open('logs.txt', 'r+', 'utf-8') as f:
            f.truncate()
        print('File clear')
    except IOError:
        print('ERROR, please check file')

root = Tk()
root.title("Календарь")
root.geometry("800x600")
root["bg"] = "#BDB76B"
notes = []
place = []
email = []
current_dates = []
current_times = []
events = []
lbl = Label(root, text="Введите дату начала события", font=("arial", 9, 'bold'), bg="#BDB76B")
lbl2 = Label(root, text="год, месяц, день", font=("arial", 9, 'bold'), bg="#BDB76B")
en = Entry(root, width=10, font=("arial", 9, 'bold'), justify="center", bg="#DA70D6")
en2 = Entry(root, width=10, font=("arial", 9, 'bold'), justify="center", bg="#DA70D6")
en3 = Entry(root, width=10, font=("arial", 9, 'bold'), justify="center", bg="#DA70D6")
btn = Button(root, text="принять", font=("arial", 9, 'bold'), bg="#ADFF2F", command=enter_first_data)
lbl.place(x=310, y=150)
lbl2.place(x=345, y=170)
en.place(x=250, y=200)
en2.place(x=350, y=200)
en3.place(x=450, y=200)
btn.place(x=360, y=250)
root.mainloop()