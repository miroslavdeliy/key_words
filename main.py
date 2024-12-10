def max_number(a, b):   #Поиск наибольшего
    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b


def empty_function():   #Пустая функция
    pass


def even_numbers(n):    #Генерация четных чисел
    count = 0
    while count <= n:
        yield count
        count += 2


def test_max_number():  #Автотест
    assert max_number(0, 3) == 3, "Ошибка, 3 должно быть больше 0!"
    assert max_number(-3, 3) == 3, "Ошибка, 3 должно быть больше -3!"
    assert max_number(5, -3) == 5, "Ошибка, 5 должно быть больше -3!"


print("Максимальное число " + str(max_number(4, 3)))
test_max_number()
empty_function()
print("Вывод четных чисел:")
for i in even_numbers(33):
    print(i)