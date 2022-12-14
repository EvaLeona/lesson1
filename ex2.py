x = int(input('Введите х'))
y = int(input('Введите у'))
z = int(input('Введите z'))


first = not (x or y or z)
second = not x and not y and not z
result = first == second


if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")