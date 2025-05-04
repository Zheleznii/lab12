values = input("Введите числа через пробел: ").split()
power = input("Введите степень: ")

if not power.lstrip('-').isdigit():
    print("Ошибка: степень должна быть целым числом.")
else:
    power = int(power)
    result = []

    for i in values:
        if i.lstrip('-').isdigit():
            result.append(str(int(i) ** power))
        else:
            result.append(i * power)

    print("Вывод:", ' '.join(result))