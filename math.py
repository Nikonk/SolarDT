import sys
Chose = 0
def outCapacity(Ia, n, A, kl):
    Ppv = Ia * n/100 * A * kl
    return (Ppv)

def KPD(nConst, B, Tpv):
    n = nConst * (1 - B*(Tpv - 48))
    return (n)

def workTempFoto(Ta, Ia, Vw):
    k0 = 30.02
    k1 = 6.28
    Tpv = Ta + Ia / (k0 + k1 * Vw)
    return Tpv

def photoCurrent(Ia, Isc, Tpv):
    Iph = Ia / 1000 * (Isc + 0.0038*(Tpv - 25))
    return Iph

def outVoltage(Ppv, Iph):
    Upv = Ppv / Iph
    return Upv

print("Введите:")
Ia = float(input('Солнечная радиацию: '))
nConst = float(input('КПД: '))
A = float(input('Площадь панели: '))
kl = 0.95
B = 0.006
Vw = float(input('Скорость ветра: '))
Ta = float(input('Температура воздуха: '))
Isc = float(input('Ток КЗ: '))
k1 = 6.28
print('Рабочая температура: '+ str(workTempFoto(Ta, Ia, Vw)))
Tpv = workTempFoto(Ta, Ia, Vw)
print('КПД преобрзователя: '+ str(KPD(nConst, B, Tpv)))
n = KPD(nConst, B, Tpv)
print('Фототок: '+ str(photoCurrent(Ia, Isc, Tpv)))
Iph = photoCurrent(Ia, Isc, Tpv)
print('Уровень выходной мощности: '+str(outCapacity(Ia, n, A, kl)))
Ppv = outCapacity(Ia, n, A, kl)
print('Выходное напряжение: ' + str(outVoltage(Ppv, Iph)))
Upv = outVoltage(Ppv, Iph)


Chose = int(input('Тип подключения(1 - последовательное; 2 - параллельное): '))
while (Chose > 3) and (Chose < 0):
    Chose = int(input('Тип подключения(1 - последовательное; 2 - параллельное): '))

Npan = int(input('Введите количество панелей: '))
if (Chose == 1):
    SumU = Upv*Npan
    sumP = Ppv*Npan
else:
    SumU = Upv
print('Мощность: ' + str(sumP))
print('Итого: '+ str(SumU))