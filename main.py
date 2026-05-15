# # # # nomes = ['Marcos', 'Gabriel','Pablo','Ricardo']

# # # # info = ['Marcos', 26, 1.88, 'Full-Stack',True]

# # # info = {
# # #     'nome' : 'Marcos',
# # #     'idade': 26,
# # #     'altura': 1.88,
# # #     'Especialidade': 'Full-Stack',
# # #     'Front-End': True

# # # }

# # # # print(type(info))

# # # # print(info['nome'])
# # # # print(info['idade'])
# # # # print(info['altura'])
# # # # print(info['Especialidade'])


# # # # info['FilmeFavorito'] = 'Curtindo a vida adoidado'

# # # # print(info)

# # # # del info['Especialidade']

# # # # print(info)
# # # # info.pop('idade')
# # # # print(info.pop('nome'))
# # # # print(info)


# # # # info = {
# # # #     'Nome' : 'Marcos'
# # # # }

# # # # info['Nome'] = 'Marcos Paulo Simoes Leite Pereira'

# # # # print(info)

# # # # info = {
# # # #     'nome' : 'Marcos',
# # # #     'email': 'exemplo@email.com'
# # # # }

# # # # if 'telefone' in info:
# # # #     print(f'possui essa chave ? {info['telefone']}')
# # # # else:
# # # #     print('nao tem essa chave')


# # # # telefone = info.get('telefone', 'nao possui')

# # # # print(telefone)

# # # # print(info['email'])

# # # # info.clear()

# # # # print(info)


# # # # info = {
# # # #     'Nome': 'Marcos',
# # # #     'Idade': 26, 
# # # #     'Altura': 1.88,
# # # #     'Especialidade': 'Full-Stack',
# # # #     'Corfavorita': 'Azul'
# # # # }


# # # # for chave in info.keys(): # mostrar so as chaves
# # # #     print(f'a chave é {chave}')

# # # # for valores in info.values(): # so os valores
# # # #     print(f'so os valores {valores}')


# # # # for chave, valor in info.items():
# # # #     print(f'as chaves sao {chave} e os valores sao {valor}')


# # # valores = {
# # #     'salario' : 2500,
# # #     'salario2' : 9000
# # # }


# # # somando = valores.values()

# # # print(sum(valores.values()))
# # # print(sum(somando))


# # # estoque = {
# # #     'notebook': 15,
# # #     'mouses': 50,
# # #     'teclados': 30,
# # #     'monitores': 8
# # # }

# # # chaves = estoque.keys() 

# # # print(list(chaves)) # transformando em lista


# # # for chave in chaves:
# # #     print(chave)

# # # if 'mouses' in chaves:
# # #     print('possui disponivel')

# # # else:
# # #     print('nao possui')


# # vendas = {
# #     'janeiro': 1500,
# #     'fevereiro': 1800,
# #     'marco': 22000,
# #     'abril': 19500,
# #     'maio': 25000
# # }

# # print(vendas.items())

# # # vendas2 = {
# # #     1: 1500,
# # #     2: 1800,
# # #     3: 22000,
# # #     4: 19500,
# # #     5: 25000
# # # }


# # # valores = vendas.values()
# # # valores2 = vendas2.values()

# # # total = sum(valores)

# # # media = total / len(vendas)

# # # maiorValor = max(valores)

# # # print(f'''
# # #       o total dos meses é {total}
# # #       a media é {media}
# # #       o maior valor é {maiorValor}
# # #       ''')

# populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000} 

# paisMaior = ''

# # populacaoMaior = 0

# # for pais, populacao in populacoes.items():
# #     if populacao > populacaoMaior:
# #         paisMaior = pais
# #         populacaoMaior = populacao
# # print(f'o pais com a maior população é {paisMaior} e sua populção é de {populacaoMaior}')



# # populacoes = {
# #     "Brasil": 215_000_000,
# #     "China": 1_400_000_000,
# #     "EUA": 333_000_000,
# #     "Índia": 1_220_000_000
# # }

# # pais_maior = max(populacoes, key=populacoes.get)
# # populacao_maior = populacoes[pais_maior]

# # print(f"O país com a maior população é {pais_maior} e sua população é de {populacao_maior}")1


# # info = {'Marcos','Gabriel','Pablo','Ricardo','Marcos','Gabriel'}

# # info.add('Walter')

# # print(info) # adicionando na posiçao aleatoria 

# # info.update(['Joao','Thigas','Juliano']) # adiciona vartios de uma vez

# # print(info)

# # info.remove('Marcos') # se tiver remove se nao da erro 

# # info.discard('Joao') # se achar ele remove se nao nao da erro 
# # print(info)

# # info.pop() # remove aleatorio 

# # print(info)

# # info.clear()

# # print(info)

# # 

# nomes = {'Marcos', 'Gabriel','Pablo','Ricardo',26}

# idades = {26,23,24,22,'Marcos'}

# unindo = nomes | idades # une as sets

# print(unindo)

# intersecao = nomes & idades # oque tem nos dois

# print(intersecao)

# diferente = nomes - idades # oque tem em um e nao tem no outro

# print(diferente)

# diferenteSimetrica = nomes ^ idades

# print(diferenteSimetrica)