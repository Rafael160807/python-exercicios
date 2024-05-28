produto = {
    1: ['Monitor LED 14" ', 599.99, 1],
    2: ['Teclado Wireless', 49.26, 1],
    3: ['Mouse Wireless', 19.90 ,1],
    4: ['Cartucho Colorido', 54.00, 2]
}
total = 0 

print(50 * '-')
print('CARRINHO DE COMPRAS')
print(50 * '-')

for cod, prod in produto.items():
    subtotal = prod[1] * prod[2]
    print(f"{prod[0]} - R$ {prod[1]:.2f}")
    total += subtotal

print(50 * '-')
print(f"Total da compra R$ {total:.2f}")
print(50 * '-')