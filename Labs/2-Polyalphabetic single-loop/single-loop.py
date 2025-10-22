base_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»"

alphabet1 = "»«><`~/\\|=+_*&^%$#@}{]['\")(-:;?!., 9876543210ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБАяюэьыъщшчцхфутсрпонмлкйизжёедгвба"
alphabet2 = "3456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ012"
alphabet3 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя@#$%^&*_+=|\\/~`<>«»0123456789 .,!?;:-()\"'[]{}"


def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""
    
    key_len = len(key)
    counter_key = 0

    for char in message:
        index = base_alphabet.find(char)

        # Получаем цифру из ключа
        key_digit = int(key[counter_key])
        
        # Выбираем алфавит based on key digit
        if key_digit == 1:
            result += alphabet1[index]
        elif key_digit == 2:
            result += alphabet2[index]
        elif key_digit == 3:
            result += alphabet3[index]

        # Переходим к следующей цифре ключа (по кругу)
        counter_key = (counter_key + 1) % key_len
    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
    key_len = len(key)
    counter_key = 0

    for char in message:
        # Получаем цифру из ключа
        key_digit = int(key[counter_key])
        
        # Выбираем алфавит based on key digit
        if key_digit == 1:
            index = alphabet1.find(char)

            result += base_alphabet[index]

        elif key_digit == 2:
            index = alphabet2.find(char)    

            result += base_alphabet[index]

        elif key_digit == 3:
            index = alphabet3.find(char)

            result += base_alphabet[index]

        # Переходим к следующей цифре ключа (по кругу)
        counter_key = (counter_key + 1) % key_len

    return result

def get_key():
    """Функция для получения ключа от пользователя"""
    while True:
        try:
            key = int(input("Введите ключ для шифрования/расшифрования при 3 разных алфавитов: "))

            key_str = str(key)
            for digit in key_str:
                if not '1' <= digit <= '3':
                    print("Ошибка: ключ должен содержать только цифры 1, 2 или 3. Попробуйте снова.")
                    break
            else:
                # Если цикл завершился без break, все цифры валидны
                return str(key)
            
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