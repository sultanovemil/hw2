import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)

    print("Исходные данные:")
    print(df.info())

    # Удаление строк с пропущенными значениями
    df.dropna(inplace=True)

    # Удаление дубликатов
    df.drop_duplicates(inplace=True)

    # Сохранение очищенных данных в выходной CSV-файл
    df.to_csv(output_file, index=False)

    # Вывод информации о очищенных данных
    print("Очищенные данные:")
    print(df.info())

if __name__ == "__main__":
    # Задаем пути к файлам
    input_file = 'data/raw_data.csv'  # Путь к входному файлу данных
    output_file = 'data/cleaned_data.csv'  # Путь к выходному файлу данных
    clean_data(input_file, output_file)
