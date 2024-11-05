# Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

dia = int(input("Digite a idade em dias: "))
ano = dia // 365
dia %= 365
mes = dia // 30
dia %= 30


print(f"Anos: {ano}")
print(f"Meses: {mes}")
print(f"Dias: {dia}")