n = int(input("Введите количество товаров: "))
i = 1
good = []

for i in range(n):
    features = dict({'name': input("Введите название: "),
                     'price': int(input("Введите цену: ")),
                     'quantity': int(input("Введите количество: ")),
                     'unit': input("Введите единицу измерения: ")})
    good.append((i + 1, features))
    i += 1
    analytics = dict({'name': features.get('name'),
                      'price': features.get('price'),
                      'quantity': features.get('quantity'),
                      'unit': features.get('unit')})

print(good)
print(analytics)

for key, value in analytics.items():
    print(f'{key}: {value}')