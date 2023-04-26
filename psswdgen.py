import random
import string

def generate_password(length, special_chars=True, numbers=True):
    """Gera uma senha aleatória de comprimento especificado"""
    characters = string.ascii_letters
    if special_chars:
        characters += string.punctuation
    if numbers:
        characters += string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Exemplo de uso
length = int(input("Digite o comprimento da senha: "))
special_chars = input("Deseja incluir caracteres especiais? (S/N)").lower() == "s"
numbers = input("Deseja incluir números? (S/N)").lower() == "s"

password = generate_password(length, special_chars, numbers)
print(password)

