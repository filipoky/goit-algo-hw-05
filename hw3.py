
import sys
from typing import List, Dict

# Парсинг одного рядка лог-файлу 
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message
    }

# Завантаження лог-файлу 
def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logs = [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        sys.exit(1)
    return [log for log in logs if log]  # Фільтруємо пусті словники

# Фільтрація логів за рівнем 
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"] == level.upper(), logs))

# Підрахунок логів за рівнями 
def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

# Виведення таблиці з підрахунком 
def display_log_counts(counts: Dict[str, int]):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<17}| {counts[level]}")

# Виведення конкретних логів за рівнем 
def display_logs(logs: List[dict], level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

# Основна логіка 
def main():
    if len(sys.argv) < 2:
        print("Використання: python hw3.py <logfile.log> [loglevel]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered = filter_logs_by_level(logs, filter_level)
        if filtered:
            display_logs(filtered, filter_level)
        else:
            print(f"\nНемає записів для рівня '{filter_level.upper()}'")

# Точка входу 
if __name__ == "__main__":
    main()



