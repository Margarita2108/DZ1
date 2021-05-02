my_percent = int(input("Введите количество процентов:  "))
if my_percent % 10 == 1:
    word = 'процент'
elif 1 < (my_percent % 10) < 5:
    word = 'процента'
else:
    word = 'процентов'
print(f'{my_percent} {word}')
