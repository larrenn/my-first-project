import random

def choose_difficulty():
    print("\nВыберите уровень сложности:")
    print("1 - Легкий (неограниченные попытки)")
    print("2 - Средний (15 попыток)")
    print("3 - Сложный (7 попыток)")
    
    while True:
        try:
            choice = int(input("Ваш выбор (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до 3")
        except ValueError:
            print("Ошибка! Введите целое число.")

# Основная логика игры
difficulty = choose_difficulty()
max_attempts = 0
if difficulty == 1:
    max_attempts = float('inf')
elif difficulty == 2:
    max_attempts = 15
else:
    max_attempts = 7

number = random.randint(1, 100)
attempts = 0

print(f"\nУгадайте число от 1 до 100! У вас {max_attempts if max_attempts != float('inf') else 'неограниченное'} попыток")

while attempts < max_attempts:
    try:
        guess = int(input("Ваша попытка: "))
        attempts += 1
        
        if guess == number:
            print(f"Поздравляем! Угадали за {attempts} попыток!")
            break
        elif guess < number:
            print("Больше!")
        else:
            print("Меньше!")
            
        if max_attempts != float('inf'):
            print(f"Осталось попыток: {max_attempts - attempts}")
    except ValueError:
        print("Ошибка! Введите целое число.")

