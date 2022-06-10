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

# Конфетки

import random
from random import randint
import time

def pause():
    time.sleep(1)
    print()

def candy_remains(candy_count, player_move =0, candy = ' >0< '):
    candy_count-=player_move
    return candy_count

def picture(count, candy = ' >0< '):
    return (candy*count)

def player_change(player):
    if player == 'Игрока ->':
       player = 'Компьютера -> '
       print()
       print(f'Ход {player }')
    else:
        print()
        player = 'Игрока ->'
        print(f'Ход {player }')
    return player
    
def move(player_move):
    while True:
        player_move = input('Возьмите от 1 до 3 конфет ')
        if not player_move.isdigit() or int(player_move) == 0:
            print()
            print('Вы ввели недопустимое значение ')
        elif(int(player_move) > 3 or int(player_move) < 1):
            print()
            print('Вы взяли недопустимое количество, попробуйте снова ')
        else:
            return int(player_move)

def comp_move():
    move = randint(1,3)
    return move

def game_start():
    while True:
        candy_count = input("Введите количество конфет ")
        if not candy_count.isdigit() or int(candy_count) <= 0:
            print()
            print('Вы ввели некорректное значение, попробуйте снова ')
            print()
        return int(candy_count)

def rock_paper_scissors():
    value = randint(1,2)
    if value == 1:
        player = 'Игрока ->'
        print()
        print('Вы ходите первым ')
    else:
        player = 'Компьютера -> '
        print()
        print('Компьютер ходит первым ')
        
        return player

print()
print("Вас приветствует игра 'Конфетки'. Игроки по очереди берут от 1 до 3 конфет. Игрок, взявший последнюю конфету - проигрывает")
pause()
candy_count = game_start()
pause()
candy = ' >0< '
player = rock_paper_scissors()
player_move = 0
computer_move = 0

print(picture(candy_count))
print()
while candy_count>0:
    print()
    if player == 'Игрока ->':
        player_move = move(player_move)
        candy_count = candy_remains(candy_count, player_move)
        pause()
        print(picture(candy_count))
        if candy_count == 1:
            player = player_change(player).replace('а','')
            print()
            print(f'{player} Компьютер взял последнюю конфету и проиграл')
            print()
            break
        elif candy_count == 0:
            player = player_change(player).replace('а','')
            print()
            print(f'{player} Вы взяли последнюю конфету и проиграли')
            print()
            break
        player = player_change(player)
    else:
        computer_move = comp_move()
        candy_count = candy_remains(candy_count, computer_move)
        pause()
        print(f'Компьютер берет {computer_move}')
        pause()
        print(picture(candy_count))
        if candy_count == 1:
            player = player_change(player).replace('а','')
            print()
            print(f'{player} Вам досталась последняя конфета, Вы проиграли')
            print()
            break
        elif candy_count == 0:
            player = player.replace('а','')
            print()
            print(f'{player} взял последнюю конфету и проиграл')
            print()
            break
        player = player_change(player)
