while True:
    n = int(input("Введите N > 0: "))
    if n > 0: break 
while n > 0:
    print(n % 10)
    n //= 10