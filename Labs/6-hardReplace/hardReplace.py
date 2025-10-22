base_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»"

def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""
    
    # Преобразуем ключ в список цифр
    key_digits = [int(d) for d in key]
    n_cols = len(key_digits)
    
    # Вычисляем количество строк
    n_rows = (len(message) + n_cols - 1) // n_cols
    
    # Заполняем таблицу по строкам
    table = []
    index = 0
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            if index < len(message):
                row.append(message[index])
                index += 1
            else:
                row.append(' ')
        table.append(row)
    
    # Определяем порядок столбцов по ключу
    column_order = sorted(range(n_cols), key=lambda x: key_digits[x])
    
    # Считываем по столбцам в заданном порядке
    for col_idx in column_order:
        for row in range(n_rows):
            result += table[row][col_idx]
    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
    # Преобразуем ключ в список цифр
    key_digits = [int(d) for d in key]
    n_cols = len(key_digits)
    
    # Вычисляем количество строк
    n_rows = (len(message) + n_cols - 1) // n_cols
    
    # Определяем порядок столбцов (такой же как при шифровании)
    column_order = sorted(range(n_cols), key=lambda x: key_digits[x])
    
    # Определяем длину каждого столбца
    full_cols = len(message) % n_cols
    if full_cols == 0:
        full_cols = n_cols
    
    col_lengths = [0] * n_cols
    for i, col_idx in enumerate(column_order):
        if i < full_cols:
            col_lengths[col_idx] = n_rows
        else:
            col_lengths[col_idx] = n_rows - 1
    
    # Заполняем таблицу по столбцам
    table = [['' for _ in range(n_cols)] for _ in range(n_rows)]
    
    index = 0
    for col_idx in column_order:
        for row in range(col_lengths[col_idx]):
            if index < len(message):
                table[row][col_idx] = message[index]
                index += 1
    
    # Считываем по строкам
    for row in range(n_rows):
        for col in range(n_cols):
            result += table[row][col]
    
    return result.rstrip() 

def get_key():
    """Функция для получения ключа от пользователя"""
    while True:
        try:
            key_input = input("Введите ключ для шифрования/расшифрования: ").strip()
            
            # Проверка на пустоту
            if not key_input:
                print("Ошибка: ключ не может быть пустым. Попробуйте снова.")
                continue
            
            # Проверка что это число
            if not key_input.isdigit():
                print("Ошибка: ключ должен содержать только цифры. Попробуйте снова.")
                continue
            
            # Проверка что нет нуля
            if '0' in key_input:
                print("Ошибка: ключ не должен содержать цифру 0. Попробуйте снова.")
                continue
            
            # Проверка что цифры не повторяются
            if len(set(key_input)) != len(key_input):
                print("Ошибка: цифры в ключе не должны повторяться. Попробуйте снова.")
                continue
            
            # Проверка минимальной длины
            if len(key_input) < 2:
                print("Ошибка: ключ должен содержать минимум 2 цифры. Попробуйте снова.")
                continue
            
            return key_input
            
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте снова.")
    

def get_message():
    """Функция для получения сообщения от пользователя"""
    while True:
        message = input("Введите сообщение для шифрования: ").strip() 
        if message:  
            return message
        else:
            print("Сообщение не может быть пустым. Попробуйте снова.")

# Главное меню
def main():
    message = get_message()
    key = get_key()
    encrypted = encrypt_message(message, key)
    print(f"Зашифрованное сообщение: {encrypted}")
            
    decrypted = decrypt_message(encrypted, key)
    print(f"Расшифрованное сообщение: {decrypted}")
            
            

# Запуск программы
if __name__ == "__main__":
    main()