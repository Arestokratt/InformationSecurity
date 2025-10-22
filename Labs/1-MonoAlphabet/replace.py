# Алфавит для заглавной и строчной буквы
alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

while True:
    try:
        key = int(input("Введите ключ для шифрования сообщения [0-33]: "))
        if 0 <= key <= 33:
            break
        else:
            print("Ошибка: число должно быть от 0 до 33 включительно. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое число. Попробуйте снова.")

while True:
    message = input("Введите сообщение: ").strip() 
    if message:  
        break
    else:
        print("Сообщение не может быть пустым. Попробуйте снова.")

result = ""
back_result = ""
# Логика кода для шифрования
for i in range(len(message)):
    if message[i] in alphabet_lower:
        index = alphabet_lower.index(message[i])
        index += key
        if (index > 32):
            index -= 32
            result += alphabet_lower[index]
        else:
            result += alphabet_lower[index]

    elif message[i] in alphabet_upper:
        index = alphabet_upper.index(message[i])
        index += key
        if (index > 32):
            index -= 32
            result += alphabet_upper[index]
        else:
            result += alphabet_upper[index]

    # Для пробелов и прочего
    else:
        result += message[i]

# Логика для расшифрования
for i in range(len(result)):
    if result[i] in alphabet_lower:
        index = alphabet_lower.index(result[i])
        index -= key
        if (index < 0):
            index += 32
            back_result += alphabet_lower[index]
        else:
            back_result += alphabet_lower[index]

    elif result[i] in alphabet_upper:
        index = alphabet_upper.index(result[i])
        index -= key
        if (index < 0):
            index += 32
            back_result += alphabet_upper[index]
        else:
            back_result += alphabet_upper[index]

    else:
        back_result += result[i]

print("Зашифрованное сообщение: ", result)
print("Расшифрованное сообщение: ", back_result)