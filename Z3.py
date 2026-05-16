c = int(input("Введите минимальную сумму инвестиций X: "))
a = int(input("Введите сумму Майкла A: "))
b = int(input("Введите сумму Ивана B: "))

if a >= c and b >= c:
    print(2)
elif a >= c:
    print("Mike")
elif b >= c:
    print("Ivan")
elif a + b >= c:
    print(1)
else:
    print(0)