def gamma_encrypt(text, key):
    if isinstance(key, str):
        key_value = sum(ord(c) for c in key)
    else:
        key_value = key

    encrypted_chars = []
    for i, char in enumerate(text):
        char_code = ord(char)
        gamma = (key_value + i * 7) % 256
        encrypted_code = char_code ^ gamma
        encrypted_char = chr(encrypted_code)
        if is_valid_char(encrypted_char):
            encrypted_chars.append(encrypted_char)
        else:
            encrypted_chars.append(char)

    return ''.join(encrypted_chars)


def gamma_decrypt(text, key):
    return gamma_encrypt(text, key)


def is_valid_char(char):
    code = ord(char)

    if ('а' <= char <= 'я') or ('А' <= char <= 'Я'):
        return True

    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        return True

    if '0' <= char <= '9':
        return True
    allowed_symbols = ' .,!?;:-_+=@#$%^&*()[]{}<>|/\\\"\''
    if char in allowed_symbols:
        return True
    return False


while True:
    print("1 - Зашифровать текст")
    print("2 - Расшифровать текст")
    print("3 - Выход")
    choice = input("Выберите действие (1/2/3): ")

    if choice == '3':
        print("Выход из программы...")
        break

    elif choice == '1' or choice == '2':
        text = input("Введите текст: ")
        key_input = input("Введите ключ: ")
        try:
            key = int(key_input)
        except ValueError:
            key = key_input

        if choice == '1':
            result = gamma_encrypt(text, key)
            print(f"Зашифрованный текст: {result}")
        else:
            result = gamma_decrypt(text, key)
            print(f"Расшифрованный текст: {result}")

    else:
        print("Неверный выбор! Попробуйте снова.")
