# #графический интерфейс с помощью tk


# import tkinter as tk
# from tkinter import messagebox
#
#
# class SplashScreen(tk.Tk):
#     def __init__(self, next_callback):
#         super().__init__()
#         self.title("Splash Screen")
#
#         self.next_callback = next_callback
#
#         self.btn_next = tk.Button(self, text="Далее", command=self.next_callback)
#         self.btn_next.pack()
#
#         self.btn_exit = tk.Button(self, text="Выход", command=self.quit)
#         self.btn_exit.pack()
#
#
# class MainWindow(tk.Tk):
#     def __init__(self, user_callback, program_callback):
#         super().__init__()
#         self.title("Main Window")
#
#         self.user_callback = user_callback
#         self.program_callback = program_callback
#
#         self.btn_user = tk.Button(self, text="О пользователе", command=self.user_callback)
#         self.btn_user.pack()
#
#         self.btn_program = tk.Button(self, text="О программе", command=self.program_callback)
#         self.btn_program.pack()
#
#
# class UserInfoWindow(tk.Tk):
#     def __init__(self, back_callback):
#         super().__init__()
#         self.title("User Info Window")
#
#         self.back_callback = back_callback
#
#         self.btn_back = tk.Button(self, text="Назад", command=self.back_callback)
#         self.btn_back.pack()
#
#
# class ProgramInfoWindow(tk.Tk):
#     def __init__(self, back_callback):
#         super().__init__()
#         self.title("Program Info Window")
#
#         self.back_callback = back_callback
#
#         self.btn_back = tk.Button(self, text="Назад", command=self.back_callback)
#         self.btn_back.pack()