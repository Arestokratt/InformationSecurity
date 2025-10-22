base_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789 .,!?;:-()\"'[]{}@#$%^&*_+=|\\/~`<>«»"

def encrypt_message(message, key):
    """Функция для шифрования сообщения"""
    result = ""
    
    key_sequence = [int(digit) for digit in str(key)]
    key_length = len(key_sequence)
    
    padding_length = (key_length - len(message) % key_length) % key_length
    padded_message = message + ' ' * padding_length
    
    for i in range(0, len(padded_message), key_length):
        block = padded_message[i:i + key_length]
        
        encrypted_block = [''] * key_length
        
        for j in range(key_length):
            encrypted_block[j] = block[key_sequence[j] - 1]
        
        result += ''.join(encrypted_block)
    
    return result

def decrypt_message(message, key):
    """Функция для расшифрования сообщения"""
    result = ""
    
    key_sequence = [int(digit) for digit in str(key)]
    key_length = len(key_sequence)
    
    for i in range(0, len(message), key_length):
        block = message[i:i + key_length]
        
        decrypted_block = [''] * key_length
        
        for j in range(key_length):
            decrypted_block[key_sequence[j] - 1] = block[j]
        
        result += ''.join(decrypted_block)
    
    return result.rstrip() 

def get_key():
    """Функция для получения ключа от пользователя"""
    while True:
        try:
            key = int(input("Введите ключ для шифрования/расшифрования: "))
            return str(key)
            
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")
    

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