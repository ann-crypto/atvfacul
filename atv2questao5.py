#Escreva uma função que: A) Receba uma frase como parametro. B) Retorne uma nova frase com cada palavra com as letras invertidas.

def inverter_palavras(frase):
    palavras = frase.split()

    frase_invertida = ' '.join([palavra[::-1] for palavra in palavras])

    return frase_invertida

frase = frase = str(input("Informe uma frase: "))
frase_invertida = inverter_palavras(frase)
print(frase_invertida)