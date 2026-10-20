s = 1000
k = 0
while True:
    print("Введите число от 0 до 25:")
    p = float(input())
    if 0 < p < 25:
        break
for i in range(1, 1000):
    k += 1
    s += s * p / 100
    if s > 1100: break
print("Месяцы:", k, "\nВклад:", s)

    
