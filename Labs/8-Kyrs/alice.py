import hashlib
import random
import sympy
def simple_rsa_demo():
    print("=== RSA ===")
    p = sympy.randprime(2 ** 256, 2 ** 512)
    q = sympy.randprime(2 ** 256, 2 ** 512)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while sympy.gcd(e, phi) != 1:
        e = sympy.randprime(2 ** 16, 2 ** 17)
    d = sympy.mod_inverse(e, phi)
    print(f"Открытый ключ: ({e}, {n})")
    print(f"Закрытый ключ: ({d}, {n})")
    print(f"Длина модуля n: {n.bit_length()} бит")
    print()
    message = input("Введите сообщение для подписи: ")
    hash_obj = hashlib.sha256(message.encode())
    hash_hex = hash_obj.hexdigest()[:8]
    hash_int = int(hash_hex, 16) % n
    print(f"Хеш сообщения: {hash_int}")
    signature = pow(hash_int, d, n)
    print(f"Подпись: {signature}")
    print()
    print("--- ПРОВЕРКА ПОДПИСИ ---")
    check_message = input("Введите сообщение для проверки: ")
    check_signature = int(input("Введите подпись для проверки: "))
    check_hash_obj = hashlib.sha256(check_message.encode())
    check_hash_hex = check_hash_obj.hexdigest()[:8]
    check_hash_int = int(check_hash_hex, 16) % n
    decrypted_hash = pow(check_signature, e, n)
    print(f"Хеш проверяемого сообщения: {check_hash_int}")
    print(f"Расшифрованный хеш из подписи: {decrypted_hash}")
    if check_hash_int == decrypted_hash:
        print("✓ Подпись ВЕРНА!")
    else:
        print("✗ Подпись НЕВЕРНА!")
if __name__ == "__main__":
    simple_rsa_demo()
