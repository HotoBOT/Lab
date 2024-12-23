def read_file():
    try:
        f = open("example.txt")
    except FileNotFoundError:
        print("Файла с названием 'example.txt' не существует, программа создаст новый файл с тем же названием,\n вы можете записать в этот файл что либо перед чтением")
        a = int(input("1.Записать текст\n2.Создать файл и закрыть программу\n"))
        if a == 2:
            f = open("example.txt", "w")
            f.write("")
            f.close()
        elif a == 1:
            f = open("example.txt", "w")
            f.write(input("Напишите что-либо:"))
            f.close()
        else:
            print("Неверный номер ввода, программа автоматически создаст файл 'example.txt' и завершит работу")
            f = open("example.txt", "w")
            f.write("")
            f.close()
    else:
        tr = int(input("Введите номер метода чтения файла:\n 1.полностью\n 2.построчно\n"))
        if tr == 1:
            with open('example.txt', 'r') as file:
                content = file.read()
            print(content)
        elif tr == 2:
            with open('example.txt', 'r') as file:
                for line in file:
                    print(line)
        else:
            print("неверный номер метода!")


read_file()
#можно доработать обработку ошибок при выборе действий, но мне лень:P