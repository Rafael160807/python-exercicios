lista_compras = []

num_produtos = int(input('Quantos produtos voce deseja adicionar?: '))

for i in range(num_produtos):
    produto = input('Nome do produto: ')
    quantidade = int(input('Quantidade: '))
    lista_compras.append([produto,quantidade])
print(lista_compras)
for produto , quantidade in lista_compras:
    print(f'Produto: {produto} - Qnt: {quantidade}')