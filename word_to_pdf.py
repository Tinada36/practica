from docx2pdf import convert
import tkinter as tk

def conv():
    try:
        data = txt.get()

        path_list = data.replace('"', '').split(".")

        convert(fr"{path_list[0]}.{path_list[1]}", fr"{path_list[0]}.pdf")
        lbl.configure(text="Успешно!")
        lbl.place(x=220, y=45)
    except Exception:
        lbl.configure(text="Ошибка конвертации!!!") 

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = tk.Tk()
root.title("Конвертер ворд в пдф")
root.geometry('500x200')
root['bg'] = 'gray'
root.wm_resizable(0, 0)
center_window(root)

lbl = tk.Label(root, text="Введи путь к файлу", font=('Arial', 9, 'bold'), bg='gray')
txt = tk.Entry(root, width=37, justify="center", font=('Arial', 9, 'bold'))
btn = tk.Button(root, text="Конвертировать", command=conv)

lbl.place(x=190, y=45)
txt.place(x=120, y=80)
btn.place(x=200, y=115)

root.mainloop()