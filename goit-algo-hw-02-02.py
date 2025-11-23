from collections import deque


def is_palindrome(text: str) -> bool:
    
    # Приводимо рядок до нижнього регістру та залишаємо лише букви/цифри
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    # Створюємо двосторонню чергу
    d = deque(cleaned)

    # Порівнюємо символи з обох кінців
    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        if left != right:
            return False

    return True


if __name__ == "__main__":
    
    print(is_palindrome("А роза упала на лапу Азора"))  # True
    print(is_palindrome("Hello"))                       # False
    print(is_palindrome("Аби ріці риба"))               # True
    print(is_palindrome("12321"))                       # True
    print(is_palindrome("Зараза"))                      # False
    print(is_palindrome("Was it a car or a cat I saw?"))  # True
