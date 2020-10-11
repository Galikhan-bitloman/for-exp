import os

paths = input("Ввести путь до директории: ") #<--- вводить с двойным \\


def obxod(paths, level=1):
    print('level= ', level, 'Content: ', os.listdir(paths))
    for i in os.listdir(paths):
        if os.path.isdir(paths + '\\' + i):
            print('    ├──  ', paths + '\\' + i)
            obxod(paths + '\\' + i, level + 1)
            print(' ├──  ', paths + '\\' + i)


obxod(paths, level=1)
