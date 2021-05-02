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