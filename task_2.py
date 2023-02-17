list_1 = input("Введите элементы списка: ").split()
i = 0

for i, el in enumerate(list_1, 1):
    print(i, el[:10])