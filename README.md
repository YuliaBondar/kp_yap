# kp_yap
Курсовой проект приложение напоминаний памятных дат

from tkinter import*
from tkinter import ttk




window = Tk()
window.title("Главная страница")
#


#window.geometry('450х530')
window.geometry('600x550')
window.resizable(width=False, height=False)
window['bg']='white'


#Вывод текста
main_label = Label(window, text="Белорусский Национальный Технический Университет", font='Arial 11 bold', bg='white', fg='black' , pady="10")
main_label2 = Label(window, text="Факультет информационных технологий и робототехники", font='Arial 10 bold', bg='white', fg='black' )
main_label3 = Label(window, text="Кафедра программного обеспечения информационных систем и технологий", font='Arial 10 bold', bg='white', fg='black' )
main_label4 = Label(window, text="Курсовая работа", font='Arial 14 bold', bg='white', fg='black', padx="120", pady="40" )
main_label5=Label(window, text="по дисциплине Языки программирования", font='Arial 11 ', bg='white', fg='black')
main_label6 = Label(window, text="Приложение напоминаний о памятных датах", font='Arial 15 bold', bg='white', fg='black', pady="10" )

otstup0=Label(window,bg='white', pady="3")
main_label7 = Label(window, text="Выполнил: Студент группы 10701222", font='Arial 11', bg='white', fg='black',padx="320", anchor="w" )
main_label8 = Label(window, text="Бондарь Юлия Владимировна", font='Arial 11', bg='white', fg='black', padx="320", anchor="w")
otstup=Label(window,bg='white', pady="3")
main_label9 = Label(window, text="Преподаватель: к.ф.-м.н.,доц.", font='Arial 11', bg='white', fg='black', padx="320", anchor="w" )
main_label10 = Label(window, text="Сидорик Валерий Владимирович" , font='Arial 11', bg='white', fg='black', padx="320", anchor="w")
main_label11 = Label(window, text="Минск, 2023", font='Arial 11 bold', bg='white', fg='black', anchor="center")
otstup1=Label(window,bg='white', pady="25")



main_label.pack()
main_label2.pack()
main_label3.pack()
main_label4.pack()
main_label5.pack()
main_label6.pack()
otstup0.pack()
main_label7.pack()
main_label8.pack()
otstup.pack()
main_label9.pack()
main_label10.pack()
otstup1.pack()
main_label11.pack()

def button_clicked():
    print("Далее")

def button_clicked2():
    print("Выход")

button_click1 = ttk.Button(window, text="Далее", command=button_clicked, width=41)
button_click1.pack(side=LEFT, pady=10,)
button_click1.configure(style="Primary.TButton")
#button_click1.configure(font='Arial 10 bold', foreground="black", borderwidth=2, relief="solid")

s1 = ttk.Style()
s1.configure("Primary.TButton", foreground="black", font=("Arial", 10, "bold"))

button_click2 = ttk.Button(window, text="Выход", command=button_clicked2, width=45)
button_click2.pack(side=LEFT, pady=10)
button_click2.configure(style="Primary.TButton",)

s2 = ttk.Style()
s2.configure("Primary.TButton", foreground="black", font=("Arial", 10))

#####картинка
image_path = "C://Users//Lenovo//Desktop//яп//кп//kp_n.png"
k_im = PhotoImage(file=image_path)
width, height = k_im.width(), k_im.height()

if width > height:
    resized_image = k_im.subsample(width // 100, width // 100)
else:
    resized_image = k_im.subsample(height // 100, height // 100)

image_label = Label(window, image=resized_image, bg='white')
image_label.place(x=100, y=290, width=150, height=120)
#####




window.mainloop()
