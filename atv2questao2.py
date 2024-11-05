import math
#Elaborar um programa que lê 3 valores a, b, c, e verifica se eles formam ou não um triângulo. Supor que os valores
#lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo.
#Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum, se a é o maior.

a = int(input("Digite um valor para um lado do triângulo: "))
b = int(input("Digite um valor para o segundo lado do triângulo: "))
c = int(input("Digite um valor para o terceiro lado do triângulo: "))

if a < b + c and b < a + c and c < a + b:
    soma = (a + b + c) / 2
    area = math.sqrt(soma * (soma - a) * (soma - b) * (soma - c))

    print(f"Os valores informados podem formar um triângulo! A área é: {area: .2f}")
else:
    print("Os valores informados NAO podem formar um triângulo!")