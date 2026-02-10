def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, salary = line.split(",")
                    total += float(salary)
                    count += 1
        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден!")
        return 0, 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0, 0
if __name__ == "__main__":
    t, a = total_salary("salary.txt")
    print(f"Результат: Всего {t}, Средняя {a}")