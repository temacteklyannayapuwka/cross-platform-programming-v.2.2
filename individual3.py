# Начальная дневная норма, 10 км
daily_distance = 10

# Изначально суммарный путь равен начальной норме
total_distance = daily_distance

# Цикл для 6 последующих дней
for _ in range(1, 7):

# Увеличиваем дневную норму на 10%
    daily_distance *= 1.1
# Добавляем увеличенную норму к суммарному пути
    total_distance += daily_distance

print(f"Суммарный путь спортсмена за 7 дней: {total_distance} км")