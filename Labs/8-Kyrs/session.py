class DESKeyGenerator:
    def __init__(self):
        self.PC1 = [
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4
        ]
        
        self.PC2 = [
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        ]
        
        self.SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    def string_to_bits(self, text):
        """Преобразование строки в битовый массив"""
        bits = []
        for char in text:
            byte = ord(char)
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)
        return bits
    
    def bits_to_string(self, bits):
        """Преобразование битового массива в строку"""
        result = ""
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                if i + j < len(bits):
                    byte = (byte << 1) | bits[i + j]
            result += chr(byte)
        return result
    
    def permute(self, bits, permutation_table):
        """Выполнение перестановки битов согласно таблице"""
        return [bits[i - 1] for i in permutation_table]
    
    def left_shift(self, bits, n):
        """Циклический сдвиг влево"""
        return bits[n:] + bits[:n]
    
    def generate_round_keys(self, key):
        """Генерация 16 раундовых ключей"""
        if isinstance(key, str):
            key_bits = self.string_to_bits(key)
        else:
            key_bits = key
        
        key_56 = self.permute(key_bits, self.PC1)
        
        C = key_56[:28]
        D = key_56[28:]
        
        round_keys = []
        
        for round_num in range(16):
            shift_count = self.SHIFT_SCHEDULE[round_num]
            C = self.left_shift(C, shift_count)
            D = self.left_shift(D, shift_count)
            
            CD = C + D
            
            round_key = self.permute(CD, self.PC2)
            round_keys.append(round_key)
        
        return round_keys
    
    def print_key_info(self, key, round_keys):
        """Вывод информации о ключах"""
        print(f"Исходный ключ: {key}")
        print(f"Длина исходного ключа: {len(self.string_to_bits(key))} бит")
        print(f"После PC-1: {56} бит")
        print(f"Длина раундовых ключей: {len(round_keys[0])} бит")
        print("\nРаундовые ключи:")
        
        for i, round_key in enumerate(round_keys):
            hex_key = self.bits_to_hex(round_key)
            print(f"Раунд {i+1:2d}: {hex_key}")
    
    def bits_to_hex(self, bits):
        """Преобразование битов в шестнадцатеричную строку"""
        hex_chars = []
        for i in range(0, len(bits), 4):
            nibble = 0
            for j in range(4):
                if i + j < len(bits):
                    nibble = (nibble << 1) | bits[i + j]
            hex_chars.append(f"{nibble:01X}")
        return "".join(hex_chars)

def get_key_from_user():
    """Функция для получения ключа от пользователя"""
    while True:
        key = input("Введите ключ (ровно 8 символов): ")
        if len(key) == 8:
            return key
        else:
            print(f"Ошибка: ключ должен содержать ровно 8 символов. Вы ввели {len(key)} символов.")
            print("Пожалуйста, попробуйте еще раз:\n")
def main():
    key_gen = DESKeyGenerator()
    
    key = get_key_from_user()  
    
    round_keys = key_gen.generate_round_keys(key)
    
    key_gen.print_key_info(key, round_keys)
    
    print("\n" + "="*50)
    print("Детальный процесс для первого раунда:")
    print("="*50)
    
    key_bits = key_gen.string_to_bits(key)
    key_56 = key_gen.permute(key_bits, key_gen.PC1)
    C = key_56[:28]
    D = key_56[28:]
    
    print(f"C0: {key_gen.bits_to_hex(C)}")
    print(f"D0: {key_gen.bits_to_hex(D)}")
    
    C1 = key_gen.left_shift(C, 1)
    D1 = key_gen.left_shift(D, 1)
    
    print(f"После сдвига:")
    print(f"C1: {key_gen.bits_to_hex(C1)}")
    print(f"D1: {key_gen.bits_to_hex(D1)}")
    
    CD = C1 + D1
    K1 = key_gen.permute(CD, key_gen.PC2)
    print(f"K1: {key_gen.bits_to_hex(K1)}")

if __name__ == "__main__":
    main()
