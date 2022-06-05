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