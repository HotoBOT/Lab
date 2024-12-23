def read_file():
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