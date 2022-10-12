# 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# o  6782 -> 23
# o  0,56 -> 11
a = float(input("Введите вещественное число: "))      
def Sum_Numbers(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum
print(f" Сумма элементов числа = {Sum_Numbers(a)} ")

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# o  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
a = int(input("Введите число: "))
s = 1
for i in range(1, a+1):
    s *= i
    print(s, end=" ")



# 3.Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму

n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')



# 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
n = 4
data = []
my_List = [i for i in range(-n,n+1)]
file = open('file.txt', 'r')
for i in file.readlines():
    data.append(int(i))
file.close()
res = 1
for i in data:
    res *= my_List[i]
print(my_List)
print(f"len - {len(my_List)}")
print(res)
    

# 5.Реализуйте алгоритм перемешивания списка.
import random as rand
list = [1,4,6,7]
rand.shuffle(list)
print(list)