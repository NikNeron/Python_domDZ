# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [2, 3, 5, 9, 3]
sum = sum([lst[x] for x in range(1, len(lst), 2)])
print(sum)