class Cipher:
    def __init__(self):
        self.alphabet = [
            "А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ",
            "Ъ","Ы","Ь","Э","Ю","Я","а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у",
            "ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"," ",".",",","-","!","?","(",")"
        ]
        self.shifted_alphabets = {}
    
    def create_shifted_alphabets(self, key):
        """Создает сдвинутые алфавиты для ключа"""
        for shift in range(1, 10):
            shifted = self.alphabet[-shift * key % len(self.alphabet):] + self.alphabet[:-shift * key % len(self.alphabet)]
            self.shifted_alphabets[shift] = shifted
    
    def encrypt(self, message, key):
        """Шифрует сообщение"""
        self.create_shifted_alphabets(key)
        result = ''
        
        for count, char in enumerate(message, 1):
            # Определяем какой алфавит использовать
            shift = self._get_shift_for_position(count)
            
            if char in self.shifted_alphabets[shift]:
                # Находим индекс в сдвинутом алфавите и берем символ из оригинального
                index_in_shifted = self.shifted_alphabets[shift].index(char)
                result += self.alphabet[index_in_shifted]
            else:
                result += char  # Если символа нет в алфавите, оставляем как есть
        
        return result
    
    def decrypt(self, encrypted_message, key):
        """Расшифровывает сообщение"""
        self.create_shifted_alphabets(key)
        original = ''
        
        for count, char in enumerate(encrypted_message, 1):
            # Определяем какой алфавит использовать
            shift = self._get_shift_for_position(count)
            
            if char in self.alphabet:
                # Находим индекс в оригинальном алфавите и берем символ из сдвинутого
                index_in_original = self.alphabet.index(char)
                original += self.shifted_alphabets[shift][index_in_original]
            else:
                original += char  # Если символа нет в алфавите, оставляем как есть
        
        return original
    
    def _get_shift_for_position(self, position):
        """Определяет номер сдвига для позиции символа"""
        if position % 9 == 0:
            return 9
        elif position % 8 == 0:
            return 8
        elif position % 7 == 0:
            return 7
        elif position % 6 == 0:
            return 6
        elif position % 5 == 0:
            return 5
        elif position % 4 == 0:
            return 4
        elif position % 3 == 0:
            return 3
        elif position % 2 == 0:
            return 2
        else:
            return 1

# Основная программа
def main():
    cipher = Cipher()
    
    message = input("Введите сообщение для шифровки: ")
    key = int(input('Введите ключ: '))
    
    # Шифрование
    encrypted = cipher.encrypt(message, key)
    print(f"Зашифрованное сообщение: {encrypted}")
    
    # Расшифрование
    decrypted = cipher.decrypt(encrypted, key)
    print(f"Расшифрованное сообщение: {decrypted}")
    
    # Проверка
    if decrypted == message:
        print("✓ Шифрование и расшифрование прошли успешно!")
    else:
        print("✗ Ошибка в шифровании/расшифровании")

if __name__ == "__main__":
    main()