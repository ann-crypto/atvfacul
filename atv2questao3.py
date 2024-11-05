# faça um programa que leia 3 números inteiros e mostre o menor deles.

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
z = int(input("Digite mais um número: "))

menor = x
if y<x and x<z:
    menor = y
if z<x and z<y:
    menor = z

print('O menor número digitado foi: {}'.format(menor))