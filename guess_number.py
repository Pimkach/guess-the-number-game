import random
import datetime

name = input('Назовите себя, представитель рода числовых провидцев!\n')
start_game = True


def update_leaderboard(attempts, name, lvl):
    filename = f'leaderboard{lvl}.txt'
    try:
        with open(filename, 'r') as f:
            records = f.readlines()
    except FileNotFoundError:
        records = []

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    new_record = f"{attempts},{current_date},{name}\n"
    records.append(new_record)

    sorted_records = sorted(records, key=lambda x: int(x.split(',')[0]))[:10]

    with open(filename, 'w') as f:
        f.writelines(sorted_records)


def display_leaderboard(lvl):
    filename = f'leaderboard{lvl}.txt'
    try:
        with open(filename, 'r') as f:
            records = f.readlines()
    except FileNotFoundError:
        print("\nЗал Славы числовых провидцев пуст.")
        return

    print("\n" + "=" * 30)
    print(f"Зал Славы числовых провидцев для уровня {lvl}:")
    print("=" * 30)
    for d, record in enumerate(records, 1):
        attempts, date, player_name = record.strip().split(',')
        print(f"{d}. {player_name}: {attempts} попыток ({date})")


def get_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Пожалуйста, введите число от {min_value} до {max_value}.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")


while start_game:
    print("\n" + "=" * 30)
    print("         УГАДАЙ ЧИСЛО")
    print("=" * 30)
    print("Выберите уровень сложности:")
    print("1. Легкий   (1-50,  10 попыток)")
    print("2. Средний  (1-100, 7 попыток)")
    print("3. Сложный  (1-1000, 12 попыток)")
    print("=" * 30)

    lvl = get_int_input("Легкий, средний, сложный? Введите цифру 1, 2, 3: ", 1, 3)

    if lvl == 1:
        MAX_NUMBER, MAX_ATTEMPTS = 50, 10
    elif lvl == 2:
        MAX_NUMBER, MAX_ATTEMPTS = 100, 7
    else:
        MAX_NUMBER, MAX_ATTEMPTS = 1000, 12

    secret_number = random.randint(1, MAX_NUMBER)
    win = False

    for i in range(MAX_ATTEMPTS):
        n = get_int_input(f'Введите число от 1 до {MAX_NUMBER}: ', 1, MAX_NUMBER)

        if n == secret_number:
            win = True
            break
        else:
            print(f'Вы не угадали число. Осталось попыток: {MAX_ATTEMPTS - i - 1}')
            print('Секретное число меньше' if n > secret_number else 'Секретное число больше')

    if win:
        print('Вы угадали секретное число! Это победа!')
        update_leaderboard(i + 1, name, lvl)
        display_leaderboard(lvl)
    else:
        print(f'Вы проиграли. Вы не угадали число. Это было число {secret_number}.')

    while True:
        end_game = input('Хотите начать новую игру? Да / Нет: ').lower()
        if end_game in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'Да' или 'Нет'.")

    start_game = (end_game == 'да')

print("Спасибо за игру! До свидания!")
