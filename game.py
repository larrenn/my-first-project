import random

def choose_difficulty():
    print("\nВыберите уровень сложности:")
    print("1 - Легкий (неограниченные попытки)")
    print("2 - Средний (15 попыток)")
    print("3 - Сложный (7 попыток)")
    print("4 - Эксперт (5 попыток)")
    
    while True:
        try:
            choice = int(input("Ваш выбор (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до 4")
        except ValueError:
            print("Ошибка! Введите целое число.")

def get_max_attempts(difficulty):
    attempts_limit = {1: float('inf'), 2: 15, 3: 7, 4: 5}
    return attempts_limit[difficulty]

# Основная логика игры
print("=" * 50)
print("      Добро пожаловать в игру 'Угадай число'!")
print("=" * 50)

difficulty = choose_difficulty()
max_attempts = get_max_attempts(difficulty)

number = random.randint(1, 100)
attempts = 0

print(f"\nУгадайте число от 1 до 100! У вас {max_attempts if max_attempts != float('inf') else 'неограниченное'} попыток")

while attempts < max_attempts:
    try:
        guess = int(input("Ваша попытка: "))
        attempts += 1
        
        if guess == number:
            print(f"🎉 Поздравляем! Вы угадали число за {attempts} попыток!")
            break
        elif guess < number:
            print("Больше!")
        else:
            print("Меньше!")
            
        if max_attempts != float('inf'):
            remaining = max_attempts - attempts
            print(f"Осталось попыток: {remaining}")
            
            if remaining == 0:
                print(f"💔 Увы! Вы исчерпали все попытки. Загаданное число было: {number}")
    except ValueError:
        print("Ошибка! Введите целое число.")
