vvod = input('Пожалуйста, ответьте на вопрос: Вы преподаватель?' '\n' 'Если да, то введите любое значение и нажмите Enter, если нет- просто нажмите Enter' '\n')
if len(vvod) == 0:
    print('Здравствуйте, вашему вниманию предстваляю решение задачи "Условная конструкция"')
else:
    print('Здравствуйте, преподаватель! Прошу проверить решение задачи:')
from time import sleep
sleep(2)

# Reshenie 1
print('Решение первое: ')
sleep(1.3)
first = int(input('Введите первое целое число:' '\n'))
second = int(input('Введите второе целое число:' '\n'))
third = int(input('Введите третье целое число:' '\n'))
sleep(0.5)
if first == second == third:
    print('Результат: код ', '3')
elif first == second or second == third or first == third:
    print('Результат: код ', '2')
else:
    print('Результат: код ', '0')

print('__________')

sleep(3)

# Reshenie 2
print('Решение второе: ')
sleep(1.3)
first = int(input('Введите первое целое число:' '\n'))
second = int(input('Введите второе целое число:' '\n'))
third = int(input('Введите третье целое число:' '\n'))
mnozhestvo = {first, second, third}
sleep(0.5)
if len(mnozhestvo) == 1:
    print('Результат: код ', '3')
elif len(mnozhestvo) == 2:
    print('Результат: код ', '2')
else:
    print('Результат: код ', '0')


print('__________')

sleep(3)

# Reshenie 3
print('Решение третье: ')
first = input('Введите три значения через Enter:' '\n')
second = input()
third = input()
mnozhestvo = {first, second, third}
if len(mnozhestvo) == 1:
    print('Результат: код ', '3')
elif len(mnozhestvo) == 2:
    print('Результат: код ', '2')
else:
    print('Результат: код ', '0')

print('На этом всё, до свидания!')