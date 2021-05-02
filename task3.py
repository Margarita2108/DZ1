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
