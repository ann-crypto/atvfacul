#Implementer uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

for num in range(1, 101):
    if primo(num):
        print(f"{num} é número primo.")
    else:
        print(f"{num} não é número primo.")