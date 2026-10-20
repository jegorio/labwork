while True:
    try: 
        n = int(input("Введите число N > 0: "))
        if n > 0: break 
        else: print("Ошибка: Число должно быть больше нуля")
    except: ValueError: print("Ошибка: Введите число")

while n > 0:
    print(n % 10)
    n //= 10