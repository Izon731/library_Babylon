def find_location(combination):
    # Преобразуем комбинацию в число
    number = int(combination)

    # Вычисляем книгу, строку и позицию
    book = number // 70
    remainder = number % 70
    line = remainder // 7
    position = remainder % 7

    return book, line, position


def generate_book(book_number):
    # Генерируем все комбинации из 4 цифр для этой книги
    combinations = [f"{i:04}" for i in range(book_number * 70, (book_number + 1) * 70)]

    # Создаём строки книги
    book = []
    for line_number in range(10):
        # Создаём строку из 10 цифр
        line = ""
        for combo in combinations[line_number * 7: (line_number + 1) * 7]:
            line += combo[:4]  # Берём первые 4 цифры комбинации
        book.append(line)

    return book


# Вводим число
combination = input("Введите число из 4 цифр: ")

# Находим местоположение
book, line, position = find_location(combination)

# Генерируем книгу
book_content = generate_book(book)

# Выводим результат
print(f"Число {combination} находится в книге {book}, строка {line}, позиция {position}.")
print(f"Содержимое книги {book}:")
for line_number, line_content in enumerate(book_content):
    print(f"Строка {line_number}: {line_content}")
