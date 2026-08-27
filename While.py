from time import sleep
from random import randint
valor = int(input('Quanto você quer sacar? '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Você sacou {totced} notas de {ced} reais')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break







Pm1000 = 0
mp = 0
mn = ' '
cont = 0
tot = 0
print('Mercado tudinho.')
while True:
    nom = str(input('Nome do produto: '))
    val = float(input('Preço do produto: '))
    tot += val
    cont += 1
    if cont == 1 or val < mp:
        mp = val
        mn = nom
    esco = ' '
    while esco not in 'SsNn':
        esco = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if val >= 1000:
        Pm1000 += 1
    
    if esco == "N":
        print(f'O valor total foi {tot}')
        print(f'{Pm1000} itens passaram de 1000 reais')
        print(f'O item mais barato que você comprou foi {mn} custando {mp}')
        break
    





M18 = 0
Hc = 0
Mm18 = 0
while True:
    print('Cadastre uma pessoa!')
    ida = int(input('Qual a idade: '))
    sexo = ' '
    escolha = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o seu sexo: [M/F]')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if ida >= 18:
        M18 += 1
    if sexo == 'M':
        Hc += 1
    if sexo == 'F' and ida < 20:
        Mm18 += 1
    if escolha == "N":
        print(f'Você cadastrou {M18} pessoas com ou mais de 18 anos, {Hc} pessoas do sexo masculino e {Mm18} mulheres com menos de 20 anos de idade.')
        break
    






print('Vamos jogar impar ou par!')
v = 0
while True:
    IoP = str(input('Impar ou par?(I/P): '))
    nmp = int(input('Agora escolhe um número: '))
    bt = randint(0, 10)
    if IoP == "I":
        if (nmp + bt) % 2 == 1:
            print(f'Você jogou {nmp} e o bot {bt}, a soma é {nmp+bt} resultando em impar então você GANHOU!')
            v += 1

        else:
            print(f'Você jogou {nmp} e o bot {bt}, a soma é {nmp+bt} resultando em par, que pena você PERDEU!')
            print(f'Você ganhou {v} vezes.')
            print('Finalizando...')
            sleep(1)
            break
    elif IoP == 'P':
        if (nmp + bt) % 2 == 0:
            print(f'Você jogou {nmp} e o bot {bt}, a soma é {nmp+bt} resultando em par então você GANHOU!')
            v += 1
        else:
            print(f'Você jogou {nmp} e o bot {bt}, a soma é {nmp+bt} que infelizmente é impar e você perdeu!')
            print(f'Você ganhou {v} vezes.')
            print('Finalizando...')
            sleep(1)
            break
    else:
        print('Digite a letra certa.')





while True:
    mul = 0
    tabu = int(input('Me fale um número para fazer tabuada (0 ou negativo finaliza o programa): '))
    if tabu <= 0:
        print('Finalizando...')
        sleep(1)
        break
    else:
        for i in range (1, 11):
            mul += 1
            print(f'{tabu} X {mul} = {tabu*mul}')





nm = 0
cont = 0
nms = 0
nm = int(input('Coloque um número(999 faz parar): '))
while True:
    if nm == 999:
        break
    cont += 1
    nms += nm
    nm = int(input('Coloque um número(999 faz parar): '))
print('No final você digitou {} números e a soma de todos eles é {} (Tirando o 999)'.format(cont, nms))


nm1 = int(input('Digite o primeiro número: '))
nm2 = int(input('Digite o segundo número: '))
esco = 0
while esco != 5: 
    esco = int(input('''Escolha uma opção:
[1] Somar
[2] Multiplicar
[3] Maior entre eles
[4] Novos números
[5] Finalizar
Sua escolha: '''))
    print('-='*10)
    if esco == 1:
        print('Somando...')
        print('-='*10)
        sleep(1)
        print('A soma entre {} e {} é {}'.format(nm1, nm2, nm1+nm2))
        print('-='*10)
    elif esco == 2:
        print('Multiplicando...')
        print('-='*10)
        sleep(1)
        print('A multiplicação de {} e {} é {}'.format(nm1, nm2, nm1*nm2))
        print('-='*10)
    elif esco == 3:
        print('Pensando...')
        sleep(1)
        if nm1 < nm2:
            print('Entre {} e {} o maior é {}'.format(nm1, nm2, nm2))
            print('-='*10)
        elif nm1 > nm2:
            print('Entre {} e {} o maior é {}'.format(nm1, nm2, nm1))
            print('-='*10)
        else: 
            print('Os dois são iguais!')
            print('-='*10)
    elif esco == 4:
        nm1 = int(input('Escolha o primeiro número de novo: '))
        print('-='*10)
        nm2 = int(input('Escolha o segundo número de novo támbem: '))
        print('-='*10)
    elif esco >= 6:
        print('Opção invalida! Tente novamente.')
        print('-='*10)
print('Finalizando...')
sleep(1)
print('Programa finalizado!')