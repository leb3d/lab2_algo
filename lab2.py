import numpy as np

# Підпрограма 1: Введення (формування) вхідних даних
def generate_data(days=365):
    # Генерація температур для вказаної кількості днів у діапазоні від -20 до +40
    temperatures = np.random.randint(-20, 41, size=days)
    return temperatures

# Підпрограма 2: Розв’язання задачі
def process_data(temperatures):
    average_temp = np.mean(temperatures)
    # Використання булевої індексації для підрахунку днів
    target_days = temperatures[temperatures > average_temp + 5]
    count_days = target_days.size
    return average_temp, count_days

# Підпрограма 3: Виведення результату
def print_results(temperatures, average_temp, count_days):
    print(f"Згенеровані температури (перші 15 днів): {temperatures[:15]} ...")
    print(f"Середня температура за рік: {average_temp:.2f} °C")
    print(f"Кількість днів, коли температура перевищувала середню на 5°C: {count_days}")

# Головна програма
def main():
    temps_array = generate_data()
    avg_temp, days_count = process_data(temps_array)
    print_results(temps_array, avg_temp, days_count)

if __name__ == "__main__":
    main()