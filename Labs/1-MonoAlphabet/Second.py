# Алфавиты для заглавных и строчных букв
alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
digits = "0123456789"   
punctuation = " .,!?;:-()\"'"

# Объединяем все символы для проверки
all_symbols = alphabet_lower + alphabet_upper + digits + punctuation

def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""
    
    for char in message:
        if char in alphabet_lower:
            index = alphabet_lower.index(char)
            index = (index + key) % 33
            result += alphabet_lower[index]
            
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            index = (index + key) % 33
            result += alphabet_upper[index]
            
        elif char in digits:
            index = digits.index(char)
            index = (index + key) % 10
            result += digits[index]
            
        elif char in punctuation:
            index = punctuation.index(char)
            index = (index + key) % len(punctuation)
            result += punctuation[index]
            
        else:
            # Если символ не поддерживается, оставляем как есть
            result += char
    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
    for char in message:
        if char in alphabet_lower:
            index = alphabet_lower.index(char)
            index = (index - key) % 33
            result += alphabet_lower[index]
            
        elif char in alphabet_upper:
            index = alphabet_upper.index(char)
            index = (index - key) % 33
            result += alphabet_upper[index]
            
        elif char in digits:
            index = digits.index(char)
            index = (index - key) % 10
            result += digits[index]
            
        elif char in punctuation:
            index = punctuation.index(char)
            index = (index - key) % len(punctuation)
            result += punctuation[index]
            
        else:
            # Если символ не поддерживается, оставляем как есть
            result += char
    
    return result

def get_key():
    """Функция для получения ключа от пользователя"""
    while True:
        try:
            key = int(input("Введите ключ для шифрования/расшифрования [0-33]: "))
            if 0 <= key <= 33:
                return key
            else:
                print("Ошибка: число должно быть от 0 до 33 включительно. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")

def get_message():
    """Функция для получения сообщения от пользователя"""
    while True:
        message = input("Введите сообщение: ").strip() 
        if message:  
            return message
        else:
            print("Сообщение не может быть пустым. Попробуйте снова.")

# Главное меню
def main():
    while True:
        print("Выберите что хотите сделать: ")
        print("1. Зашифровать сообщение")
        print("2. Расшифровать сообщение")
        print("3. Выйти из программы")
        
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Шифрование ---")
            key = get_key()
            message = get_message()
            encrypted = encrypt_message(message, key)
            print(f"Зашифрованное сообщение: {encrypted}")
            
        elif choice == "2":
            print("\n--- Дешифрование ---")
            key = get_key()
            message = get_message()
            decrypted = decrypt_message(message, key)
            print(f"Расшифрованное сообщение: {decrypted}")
            
        elif choice == "3":
            print("Выход из программы...")
            break
            
        else:
            print("Ошибка: выберите действие от 1 до 3.")

# Запуск программы
if __name__ == "__main__":
    main()