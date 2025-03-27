n1 = int(input('f1:'))
n2 = int(input('f2:'))
n3 = int(input('f3:'))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

else:
    n1 == n2 == n3
    print('todos os numeros sao iguais, somando cinco a todos')

print(menor + 5) 
