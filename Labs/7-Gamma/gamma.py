base_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»"

def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""
    
     # Подготавливаем гамму: повторяем ключ до длины сообщения
    gamma = ""
    gamma_index = 0
    
    # Создаем гамму только для символов, присутствующих в алфавите
    for char in message:
        if char in base_alphabet:
            gamma += key[gamma_index % len(key)]
            gamma_index += 1
        else:
            gamma += char  # Для символов не из алфавита
    
    # Шифруем сообщение методом гаммирования
    message_index = 0
    for i in range(len(message)):
        if message[i] in base_alphabet:
            # Находим индексы символа сообщения и гаммы
            message_char_index = base_alphabet.index(message[i])
            gamma_char_index = base_alphabet.index(gamma[message_index])
            
            # Шифруем: (сообщение + гамма) mod длина_алфавита
            encrypted_index = (message_char_index + gamma_char_index) % len(base_alphabet)
            result += base_alphabet[encrypted_index]
            message_index += 1
        else:
            # Символы не из алфавита остаются без изменений
            result += message[i]
    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
# Подготавливаем гамму (так же как при шифровании)
    gamma = ""
    gamma_index = 0
    
    for char in message:
        if char in base_alphabet:
            gamma += key[gamma_index % len(key)]
            gamma_index += 1
        else:
            gamma += char
    
    # Расшифровываем сообщение
    message_index = 0
    for i in range(len(message)):
        if message[i] in base_alphabet:
            # Находим индексы символа шифртекста и гаммы
            encrypted_char_index = base_alphabet.index(message[i])
            gamma_char_index = base_alphabet.index(gamma[message_index])
            
            # Расшифровываем: (шифртекст - гамма) mod длина_алфавита
            decrypted_index = (encrypted_char_index - gamma_char_index) % len(base_alphabet)
            result += base_alphabet[decrypted_index]
            message_index += 1
        else:
            # Символы не из алфавита остаются без изменений
            result += message[i]
    
    return result.rstrip()


def get_key():
    """Функция для получения ключа от пользователя"""
    while True:
        key= input("Введите ключ для шифрования/расшифрования: ").strip() 
        if key:  
            return key
        else:
            print("Сообщение не может быть пустым. Попробуйте снова.")
    

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