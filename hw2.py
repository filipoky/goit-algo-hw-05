
from typing import Callable

def generator_numbers(text: str):
    for word in text.split():            # Розбиваємо вхідний текст на окремі слова
        try:                             # Пробуємо перетворити слово у число float
            yield float(word)            # Якщо вдалося — повертаємо значення через yield
        except ValueError:               # Якщо слово не є числом — пропускаємо його
            continue

def sum_profit(text: str, func: Callable[[str], any]) -> float:
    return sum(func(text))               # Викликаємо func(text) як генератор і підсумовуємо всі значення


# Приклад використання:
if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

