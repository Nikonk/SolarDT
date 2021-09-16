def addPanel(Upv):
    i = 0
    parPan = []
    cor = False
    addPan = ''
    con = 0

    while (con != '1') and (con != '2') and (con != '3'):
        con = input('Выбрать тип соединение 1-последовательное, 2-параллельное, 3-смешанное: ')
        if (con != '1') and (con != '2') and (con != '3'):
            print('Некоррекный ввод')
            nPan = float(input('Добавить количество последовательных панелей: '))
    if con == '1':
        nPan = float(input('Введите количество последовательно подключенных панелей: '))
        print('Напряжение: ' + str(nPan * Upv))
    elif con == '2':
        nPan = float(input('Введите количество параллельно подключенных панелей: '))
        print('Напряжение: ' + str(Upv))
    elif con == '3':
        nPan = float(input('Введите количество последовательно подключенных панелей: '))
        while nPan < nPan + 1:
            while cor == False:
                x = input('Введите количество параллельно подключенных панелей: ')
                cor = x.isdigit()
                if cor == False:
                    print('Некоррекный ввод')
            parPan.insert(i, int(x))
            nPan = nPan + 1
            i = i + 1

            while (addPan != 'y') and (addPan != 'n'):
                addPan = input('Добавить ещё параллельное соединение? y/n: ')
                if (addPan != 'y') and (addPan != 'n'):
                    print('Некоррекный ввод')
            if addPan == 'n':
                break
        print('Напряжение для панели' + str() + ': ' + str(nPan * Upv))

    return nPan