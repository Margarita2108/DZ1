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
