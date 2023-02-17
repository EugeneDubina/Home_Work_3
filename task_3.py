my_list = [7, 5, 3, 3, 2]
print(f'Текущий список {my_list}')
new_el = int(input("Введите число от 0 до 100: "))
for i in range(len(my_list)):
    if my_list[i] == new_el:
        my_list.insert(i+1, new_el)
        break
    elif new_el > my_list[0]:
        my_list.insert(0, new_el)
    elif new_el < my_list[-1]:
        my_list.append(new_el)
    elif my_list[i + 1] < new_el < my_list[i]:
        my_list.insert(i + 1, new_el)
        break

print(f'Пользователь ввел число {new_el}. Результат: {my_list}')
