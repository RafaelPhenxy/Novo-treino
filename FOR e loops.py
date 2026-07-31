from random import randint
# -*- coding: utf-8 -*-
#i
from time import sleep
nm = 11
for u in range (10, 0, -1):
    print(u)
    sleep(0)
print('TEMPO ACABOU!')
#
for i in range (2, 52, 2):
    print(i, end=(' '))
print('Todos os números pares até 50')
#
cont = 0
somato = 0
for o in range (1, 500, 2):
    if o % 3 == 0:
        somato = somato + o
        cont = cont + 1
print('A soma de todos os numéros impares multiplos de 3 até 500 é {}, foram somados {} números'.format(somato, cont))

#
nb = int(input('Coloque 1 número para a tabuada até 10: '))
for p in range (1, 11):
    print('{} x {:2} = {}'.format(nb, p, nb*p))
#
soma = 0
cont = 0
for q in range (1,7):
    n = int(input('Fale um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('O somatorio desses números é: {} e foi informado {} números pares.'.format(soma, cont))
#
num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1,):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto [letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
#
sx = str(input('Informe seu sexo: ')).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input('Errado. Informe o correto: ')).strip().upper()[0]
print(('Seu sexo é {}, obrigado.'.format(sx)))
#
pc = randint(0, 10)
nb = int(input('Tenta adivinhar o número que eu pensei: '))
while nb != pc:
    if nb < pc:
        nb = int(input('Tenta de novo um pouco maior: '))
    elif nb > pc:
        nb = int(input('Tenta de novo um pouco menor: '))
print('Parabens você acertou: {}'.format(nb))