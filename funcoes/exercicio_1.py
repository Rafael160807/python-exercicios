def calcularMedia(nota1,nota2,nota3,nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media 


print('Calculadoa de Média')
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
n3 = float(input('Digite a 3º nota: '))
n4 = float(input('Digite a 4º nota: '))
m = calcularMedia(n1,n2,n3,n4)
print(f"Sua média é {m}")