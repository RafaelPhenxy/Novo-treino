#tuplas
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Refri')
print(lanche[1])
print(lanche[0])
print(lanche[-2])
print(lanche[0:3])
print(lanche[2:])
print(lanche[:3])
for c in lanche:
    print(f'Eu vou pedir um {c}')

for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont}({pos})')
print(len(lanche))
print(sorted(lanche))
a = (2, 9, 1)
b = (7, 6, 2, 5, 4)
c = a + b
print(c)
print(len(c))
print(c.count(2))
print(c.index(9))
del (c)

#Exercicios
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesste', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input("Escolha um número entre 0 a 20: "))
    if 0 <= num <= 20:
        print(f'Você digitou {extenso[num]}')
        break
    else:
        esco = ' '
        print('Tente novamente')
        while esco not in 'SsnN':
            esco = str(input('Quer continuar? S/N ')).upper().strip()[0]
        if esco == 'N':
            print('Encerrando...')
            break
