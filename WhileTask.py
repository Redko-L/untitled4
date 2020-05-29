a = 4
b = 15
c = 2
while a < b:
    print(a)
    a += c
    if a < b:
        print("Значение А " + "Пока что нет")
else:
    print("Дождались! " + "Финальный А")