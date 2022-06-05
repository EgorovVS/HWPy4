# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя



def to_ascending_sequence(numbers_list, next_element):
    new_list = []
    for i in range (len(numbers_list)):
     if numbers_list[i]>next_element:
        next_element =numbers_list[i]
        new_list.append(next_element)
    return new_list

numbers_list = [1, 5, 2, 3, 4, 6, 1, 7]
next_element=0
print(to_ascending_sequence(numbers_list, next_element))

# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

import random
from random import randint
with open('task2.txt','w') as doc:
    random_numbers = ''
    random_numbers = ''.join(map(str,([randint(1, 11) for i in range(10)])))
    doc.write(random_numbers)
    print(random_numbers)
with open('task2.txt','r+') as doc:
    numbers = ''.join(map(str,sorted(doc.read())))
with open('task2.txt','w') as doc:   
    doc.write(str(numbers))

# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 

with open('1Kints.txt', 'r') as doc:
    numbers = doc.read().strip().split()
first = []
second = []
third = []
for el in range (len(numbers)):
   for elem in range (len(numbers)):
       for element in range (len(numbers)):
           if int(numbers[el])+int(numbers[elem])+int(numbers[element]) == 0:
               first.append(numbers[el])
               second.append(numbers[elem])
               first.append(numbers[element])
result = zip(first, second, third)
print(list(result))

# Пиво

def beeramid(bonus, beer_price):
    beer_cans = int(bonus/beer_price)
    level = 1
    cans = 0
    while beer_cans>=cans:
        level_count = level**2
        beer_cans-=level_count
        level+=1
        cans+= level_count  
        print(level_count)
    return level

bonus = 1500
beer_price = 2
result = beeramid(bonus,beer_price)
print(result)