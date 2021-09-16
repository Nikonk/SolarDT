import mathPack
import calcPanel

Ia = float(input('Солнечная радиация: '))
Ta = float(input('Температура воздуха: '))
Vw = float(input('Скрорость ветра: '))
A = float(input('Общая площадь солнечных панелей: '))
nConst = float(input('Паспортное значение КПД: '))
Isc = float(input('Ток короткого замыкания: '))
B = 0.004
kl = 0.85
k1 = 0.00038
Pan = []

# Расчет для одной панели
Tpv = mathPack.workTempFoto(Ta, Ia, Vw)
print('Tpv = ' + str(Tpv))
n = mathPack.KPD(nConst, B, Tpv)
print('КПД = ' + str(n))
Iph = mathPack.photoCurrent(Ia, Isc, Tpv, k1)
print('Ipv = ' + str(Iph))
Ppv = mathPack.outCapacity(Ia, n, A, kl)
print('Ppv = ' + str(Ppv))
Upv = mathPack.outVoltage(Ppv, Iph)

Pan.append(calcPanel.addPanel(Upv))

y = 'y'

while y == 'y':
    y = input('Добавить модуль? y/n: ')
    if y == 'y':
        Pan.append(calcPanel.addPanel(Upv))
    elif y == 'n':
        break
    else:
        y = 'y'
        print('Некорректный ввод!')
