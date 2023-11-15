import random

def criar_senha():
    senha = ""
    alfabeto_menos = "qwertyuiopasdfghjklçzxcvbnm"
    alfabeto_mais = "QWERTYUIOIPASDFGHJKLÇZXCVBNM"
    numeros = "0123456789"
    simbolos = "!@#$%&*?*"
    for digito in range (2):
        aleatorio1 = random.choice(alfabeto_mais)
        senha += aleatorio1
    for digito in range (2):
        aleatorio1 = random.choice(alfabeto_menos)
        senha += aleatorio1
    for digito in range (2):
        aleatorio2 = random.choice(numeros)
        senha += aleatorio2
    for digito in range (2):
        aleatorio3 = random.choice(simbolos)
        senha += aleatorio3

    print("Senha Gerada: " + senha)

criar_senha()