numeros = []
par = 0
impar = 0
quantidade = int(input('quantos numeros deseja colocar ? '))

for n in range(quantidade):
    numero = int(input('Digite um numero : '))
    if numero % 2 == 0:
        par += 1 
        numeros.append(numero)
    else:
        impar += 1
        numeros.append(numero)

soma = sum(numeros)
quantidade = len(numeros)
print(f'''
quantidade de elementos: {quantidade}
soma: {soma}
média: {soma  / quantidade}
quantidade de pares: {par}
quantidade de impares: {impar}
''')
