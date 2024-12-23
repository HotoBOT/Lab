f = open("user_input.txt", "a")
a = input("Введите текст, который будет добавлен в файл:")
f.write(a)
f.close()
