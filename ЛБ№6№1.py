class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self):
        self.__password = input("Введите новый пароль:")

    def check_password(self, password):
        return self.__password == password

pw = UserAccount("Nick", "nick@email.com", "qwerty4856")
m = int(input("Хотите сменить текущий пароль:\n1.Да\n2.Нет\n"))
if m == 1:
    pw.set_password()
    password_to_check = input("Введите пароль: ")
    print(pw.check_password(password_to_check))
elif m == 2:
    password_to_check = input("Введите пароль: ")
    print(pw.check_password(password_to_check))
else:
    print("неверный ввод!")