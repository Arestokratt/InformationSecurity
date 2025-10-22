base_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»"

def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""

    key_length = len(key)
    alphabet_length = len(base_alphabet)
    
    for i, char in enumerate(message):
        if char in base_alphabet:
            char_index = base_alphabet.index(char)

            key_index = base_alphabet.index(key[i % key_length])

            encrypted_index = (char_index + key_index) % alphabet_length

            result += base_alphabet[encrypted_index]
        else:

            res 

    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
    key_length = len(key)
    alphabet_length = len(base_alphabet)
    
    for i, char in enumerate(message):
        if char in base_alphabet:

            char_index = base_alphabet.index(char)

            key_index = base_alphabet.index(key[i % key_length])

            decrypted_index = (char_index - key_index) % alphabet_length

            result += base_alphabet[decrypted_index]
        else:

            result += char

    return result

def get_key():
    """Функция для получения ключа от пользователя"""
    key = input("Введите ключ для шифрования/расшифрования: ")
    return key
    

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