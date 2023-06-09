# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трехзначное число')
N = str(input())
if len(N) == 3:
    sum = int(N[0]) + int(N[1]) + int(N[2])
    print(f'{N} -> {sum}')
else:
    print('Введено не трехзначное число')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print('Введите количество журавликов, сделанное тремя друзьями: ')
S = int(input())
if S%3 == 0 and (S/3)%2 == 0:
    P=int((S/3)/2)
    K = int((P+P)*2)
    C = int(S - P - K)
    print(f'{S} -> {P} {K} {C}')
else:
    print('Невозможно дать ответ в целых числах')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

print('Введите шестизначный номер билета')
number = str(input())
if len(number) == 6:
    sum1 = int(number[0]) + int(number[1]) + int(number[2])
    sum2 = int(number[3]) + int(number[4]) + int(number[5])
    if sum1 == sum2:
        print(f'{number} -> yes')
    else:
        print(f'{number} -> no')
else:
    print('Введен некорректный номер билета, в нем должно быть 6 цифр')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
print('Введите число долек по горизонтали:')
n = int(input())
print('Введите число долек по вертикали:')
m = int(input())
print('Введите сколько долек нужно отломить:')
k = int(input())
if n*m != k:
    if k%n == 0 or k%m == 0:
        print(f'{n} {m} {k} -> yes')
    else:
        print(f'{n} {m} {k} -> no')
else:
    print('Чтобы получить столько долек ломать шоколадку не потребуется')