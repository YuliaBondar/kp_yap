

# #логика программы
# from model import UserModel, ProgramModel
# from view import SplashScreen, MainWindow, UserInfoWindow, ProgramInfoWindow
#
#
# class Controller:
#     def __init__(self):
#         self.user_model = UserModel()
#         self.program_model = ProgramModel()
#
#         self.splash_screen = SplashScreen(self.show_main)
#         self.main_window = MainWindow(self.show_user, self.show_program)
#         self.user_info_window = UserInfoWindow(self.show_main)
#         self.program_info_window = ProgramInfoWindow(self.show_main)
#
#         self.show_splash()
#
#     def show_splash(self):
#         self.splash_screen.mainloop()
#
#     def show_main(self):
#         self.splash_screen.destroy()
#         self.main_window.mainloop()
#
#     def show_user(self):
#         self.main_window.destroy()
#         self.user_info_window.mainloop()
#
#     def show_program(self):
#         self.main_window.destroy()
#         self.program_info_window.mainloop()
#
#
# if __name__ == "__main__":
#     app = Controller()