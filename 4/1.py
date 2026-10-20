p = 12000
r = 50
g = 9.81
def f(v):
    return (p + ((p / g) * (((v / 3.6)**2) / r)))
print("V  F")
for i in range(25, 71, 5):
    print(i, f(i))