
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage

class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash Screen")
        self.geometry("650x550")
        self.config(bg="white")

        self.label1 = tk.Label(self, text="Белорусский национальный технический университет",
                               font=("Arial", 14, "bold"),bg='white')
        self.label1.pack(pady=(10, 10))

        self.label2 = tk.Label(self, text="Факультет информационных технологий и робототехники",
                               font=("Arial", 11, "bold"),bg='white')
        self.label2.pack()

        self.label3 = tk.Label(self, text="Кафедра программного обеспечения информационных систем и технологий",
                               font=("Arial", 11, "bold"),bg='white')
        self.label3.pack()

        self.label4 = tk.Label(self, text="Курсовая работа",
                               font=("Arial", 20, "bold"),bg='white')
        self.label4.pack(pady=(40, 10))

        self.label5 = tk.Label(self, text="по дисциплине Языки программирования",
                               font=("Arial", 11),bg='white')
        self.label5.pack(pady=(20, 10))

        self.label6 = tk.Label(self, text="Приложение напоминаний о памятных датах",
                               font=("Arial", 13, "bold"),bg='white')
        self.label6.pack(pady=(3, 20))

        self.label7 = tk.Label(self, text="Выполнил: Студент группы 10701222", font='Arial 11',bg='white')
        self.label7.pack(  pady=2, padx=10, anchor="e")
        self.label8 = tk.Label(self, text="Бондарь Юлия Владимировна", font='Arial 11',bg='white')
        self.label8.pack( padx=55, anchor="e")

        self.otstup1 = tk.Label(self, pady="3", bg="white")
        self.otstup1.pack()

        self.label9 = tk.Label(self, text="Преподаватель: к.ф.-м.н.,доц.", font='Arial 11',bg='white')
        self.label9.pack(pady=2, padx=57, anchor="e")
        self.label10 = tk.Label(self, text="Сидорик Валерий Владимирович", font='Arial 11',bg='white')
        self.label10.pack(padx=37, anchor="e")

        self.otstup2 = tk.Label(self, pady="20", bg="white")
        self.otstup2.pack()

        self.label11 = tk.Label(self, text="Минск, 2023", font='Arial 11 bold', anchor="center",bg='white')
        self.label11.pack(pady=5)




        self.next_button = tk.Button(self, text="Далее", font='Arial 13', command=self.open_main_window)
        self.next_button.pack(side="left", padx=50)
        self.next_button.place(x=3, y=508, width=320, height=30)

        self.exit_button = tk.Button(self, text="Выход", font='Arial 13', command=self.exit_application)
        self.exit_button.pack(side="right", padx=50)
        self.exit_button.place(x=327, y=508, width=320, height=30)


        #картинка
        self.image_path = "C://Users//Lenovo//Desktop//яп//кп//unnamed.png"
        image = Image.open(self.image_path)
        resized_image = image.resize((200, 200))  # Resize the image to 150x120 pixels

        self.k_im = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(self, image=self.k_im)
        image_label.place(x=90, y=280, width=150, height=150)



    def open_main_window(self):
        self.destroy()
        MainWindow(self.master)

    def exit_application(self):
        if messagebox.askokcancel("Выход из приложения", "Вы уверены, что хотите выйти?"):
            self.master.destroy()


class MainWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Главное окно")
        self.geometry("650x550")

        # Create a button with the image
        self.profile_button = tk.Button(self, text="О авторе", command=self.open_profile_window)
        self.profile_button.place(x=10, y=475, width=100, height=50)

        self.about_button = tk.Button(self, text="О программе", command=self.open_about_window)
        self.about_button.place(x=120, y=475, width=100, height=50)

        def highlight_button(event):
            self.about_button.config(bg='light blue')  # Change the background color of the button when mouse enters

        def unhighlight_button(event):
            self.about_button.config(bg='SystemButtonFace')  # Restore the default background color when mouse leaves

        self.about_button = tk.Button(self, text="Назад", font='Arial 13', command=self.open_splash_screen)
        self.about_button.pack(anchor='sw')
        self.about_button.place(x=540, y=475, width=100, height=50)

        self.about_button.bind("<Enter>", highlight_button)  # Bind highlight_button to mouse enter event
        self.about_button.bind("<Leave>", unhighlight_button)



        def highlight_button(event):
            self.back_button.config(bg='light blue')  # Change the background color of the button when mouse enters

        def unhighlight_button(event):
            self.back_button.config(bg='SystemButtonFace')  # Restore the default background color when mouse leaves

        self.back_button = tk.Button(self, text="Назад", font='Arial 13', command=self.open_splash_screen)
        self.back_button.pack(anchor='sw')
        self.back_button.place(x=540, y=475, width=100, height=50)

        self.back_button.bind("<Enter>", highlight_button)  # Bind highlight_button to mouse enter event
        self.back_button.bind("<Leave>", unhighlight_button)  # Bind unhighlight_button to mouse leave event



    def open_splash_screen(self):
        self.destroy()
        SplashScreen(self.master)

    def open_profile_window(self):
        self.destroy()
        ProfileWindow(self.master)

    def open_about_window(self):
        self.destroy()
        AboutWindow(self.master)





class ProfileWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("О авторе")
        self.geometry("450x550")


        #картинка
        self.image_path = "C://Users//Lenovo//Desktop//яп//кп//photo1.png"
        image = Image.open(self.image_path)
        resized_image = image.resize((270, 320))
        self.k_im = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(self, image=self.k_im)
        image_label.place(x=75, y=10, width=290, height=320)

        text_label = tk.Label(self, text="Автор", font=("Arial", 13, "bold"), anchor="center")
        text_label.place(x=190, y=340)

        text_label1 = tk.Label(self, text="Студентка группы 10701222", font=("Arial", 13, "bold"), anchor="center",
                               justify="center")
        text_label1.place(x=105, y=360)

        text_label2 = tk.Label(self, text="Бондарь Юлия Владимировна", font=("Arial", 13, "bold"), anchor="center",
                               justify="center")
        text_label2.place(x=90, y=380)

        text_label3 = tk.Label(self, text="uliabondar359@gmail.com", font=("Arial", 13, "bold"), anchor="center",
                               justify="center")
        text_label3.place(x=110, y=400)



        def highlight_button(event):
            self.back_button.config(bg='light blue')  # Change the background color of the button when mouse enters

        def unhighlight_button(event):
            self.back_button.config(bg='SystemButtonFace')  # Restore the default background color when mouse leaves

        self.back_button = tk.Button(self, text="Назад", font='Arial 13', command=self.open_main_window)
        self.back_button.pack(anchor='center', padx=10)
        self.back_button.place(x=70, y=490, width=320, height=30)

        self.back_button.bind("<Enter>", highlight_button)  # Bind highlight_button to mouse enter event
        self.back_button.bind("<Leave>", unhighlight_button)  # Bind unhighlight_button to mouse leave event


    def open_main_window(self):
        self.destroy()
        MainWindow(self.master)





class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("О программе")
        self.geometry("600x500")

        self.label = tk.Label(self, text="Приложение напоминаний о памятных датах",font=("Arial", 13, "bold"), anchor="center")
        self.label.pack()

        text_label = tk.Label(self, text="Программа позволяет:", font=("Arial", 13))
        text_label.place(x=290, y=30)

        text_label1 = tk.Label(self, text="1.Устанавливать памятную дату.", font=("Arial", 11), anchor="center",
                               justify="center")
        text_label1.place(x=290, y=60)
        text_label1 = tk.Label(self, text="2.Установка напоминания на день и время.", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=80)
        text_label1 = tk.Label(self, text="3.Просмотр списка памятных дат.", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=105)
        text_label1 = tk.Label(self, text="4.Управление списком памятных дат\n(редактировать, добавлять, удалять).", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=130)
        text_label1 = tk.Label(self, text="5.Поиск памятных дней (год или дата \nили по названию памятных дней).", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=173)
        text_label1 = tk.Label(self, text="6.Фильтрация памятных дат (фильтрация по \nпараметрам, имени, названии, дате и т.д.).", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=197)
        text_label1 = tk.Label(self, text="7.Вывод уведомления пользователю о \nпамятной дате.", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=290, y=240)
        text_label1 = tk.Label(self, text="8. Давать возможность пользователю о от-\nметке, что дата прошла или была отмечена.", font=("Arial", 11),
                               anchor="center",
                               justify="center")
        text_label1.place(x=286, y=280)

        text_label2 = tk.Label(self, text="9.Возможно изменение настроек.", font=("Arial", 11), anchor="center",
                               justify="center")
        text_label2.place(x=288, y=325)

        text_label2 = tk.Label(self, text="10.Сохранять памятные даты, от пользовате-\nля в в бд или файле.При запуске программы \nсохранять раньше заполненные данные.", font=("Arial", 11), anchor="center",
                               justify="center")
        text_label2.place(x=285, y=355)

        text_label2 = tk.Label(self,text="11.Возможная отправка по электронной почте.",
                               font=("Arial", 11), anchor="center",
                               justify="center")
        text_label2.place(x=280, y=425)


        #Картинка
        self.image_path = "C://Users//Lenovo//Desktop//яп//кп//calend.png"
        image = Image.open(self.image_path)
        resized_image = image.resize((270, 320))
        self.k_im = ImageTk.PhotoImage(resized_image)

        image_label = tk.Label(self, image=self.k_im)
        image_label.place(x=10, y=110, width=270, height=280)



        #кнопка
        def highlight_button(event):
            self.back_button.config(bg='light blue')  # Change the background color of the button when mouse enters

        def unhighlight_button(event):
            self.back_button.config(bg='SystemButtonFace')  # Restore the default background color when mouse leaves

        self.back_button = tk.Button(self, text="Назад", font='Arial 13', command=self.open_main_window)
        self.back_button.pack(anchor='sw')
        self.back_button.place( x=10, y=450, width=70, height=30)

        self.back_button.bind("<Enter>", highlight_button)  # Bind highlight_button to mouse enter event
        self.back_button.bind("<Leave>", unhighlight_button)  # Bind unhighlight_button to mouse leave event

    def open_main_window(self):
        self.destroy()
        MainWindow(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Скрытие корневого окна

    splash_screen = SplashScreen(root)
    root.mainloop()












