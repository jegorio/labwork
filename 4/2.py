s = 1000
k = 0

while True:
    try:
        p = float(input("Введите число от 0 до 25:"))
        if 0 < p < 25: break
        else: print("Ошибка: Должно быть число от 0 до 25")
    except ValueError: print("Ошибка: Введите число")

for i in range(1, 1000):
    k += 1
    s += s * p / 100
    if s > 1100: break
print("Месяцы:", k, "\nВклад:", s)