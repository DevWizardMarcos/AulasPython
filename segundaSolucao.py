numeros = [ ]

par = 0
impar = 0

while True:
    numero = int(input('Digite um numero : '))
    if numero == 0:
        print(f'a lista ficou {numeros}')
        break 
    else:
        if numero % 2 == 0:
            par += 1 
            numeros.append(numero)
        else:
            impar += 1 
            numeros.append(numero)

total = sum(numeros)
quantidade = len(numeros)
media = total / quantidade
print(f'''
    
o total de numeros é {total}
a quantidade de elementos é {quantidade}
a media é {media:.2f}
possui {par} numeros pares 
possui {impar} numeros impares 

''')