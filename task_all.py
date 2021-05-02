# 1 задание 
duration = int(input("Введите колличество секунд:  "))
year = duration // 31536000
dey = (duration % 31536000) // 86400
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
sec = duration % 60

if year > 0:
    print(f"{year} г {dey} дн {hours} час {minutes} мин {sec} сек")
elif dey > 0:
    print(f"{dey} дн {hours} час {minutes} мин {sec} сек")
elif hours > 0:
    print(f"{hours} час {minutes} мин {sec} сек")
elif minutes > 0:
    print(f"{minutes} мин {sec} сек")
else:
    print(f"{sec} сек")

# 2 задание 
numbers = []
for idx in range(1, 1000, 2):
    numbers.append((idx ** 3))
print(numbers)


sum_number = 0
for digit in numbers:
    number = 0
    while digit >= 1:
        i = digit % 10
        digit //= 10
        number += i
    if number % 7 == 0:
        sum_number += number
print(sum_number)

sum_number = 0
for digit in numbers:
    digit += 17
    number = 0
    while digit >= 1:
        i = digit % 10
        digit //= 10
        number += i
    if number % 7 == 0:
        sum_number += number
print(sum_number)

# 3 задание 
my_percent = int(input("Введите количество процентов:  "))
if my_percent % 10 == 1:
    word = 'процент'
elif 1 < (my_percent % 10) < 5:
    word = 'процента'
else:
    word = 'процентов'
print(f'{my_percent} {word}')

my_percent_list = [15, 1, 3, 7, 4, 20]
for my_percent in my_percent_list:
    if my_percent % 10 == 1:
        word = 'процент'
    elif 1 < (my_percent % 10) < 5:
        word = 'процента'
    else:
        word = 'процентов'
    print(f'{my_percent} {word}')
