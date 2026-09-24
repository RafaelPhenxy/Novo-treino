
lista = []
while True:
    num = (int(input('Escolha um número: ')))
    if num not in lista:
        lista.append(num)
    elif num in lista:
        print('Não vou colcar esse número duplicado')
    esco = str(input('Quer continuar?(S/N): ')).upper().strip()[0]
    while esco not in 'SsNn':
            print('Escreva S ou N')
            esco = str(input('Quer continuar?(S/N): ')).upper().strip()[0]
    if esco == 'N':
        break
print(f'Você digitou os números {sorted(lista)}')


#
listn = []
listm = []
listme = []
for o in range(0,5):
    listn.append(int(input('Fale um valor: ')))
for p, va in enumerate(listn):
    if va == max(listn):
        listm.append(p)
    if va == min(listn):
        listme.append(p)
print(*listn)
print(f'O maior número foi {max(listn)} e ele tava na posição: ', *listm)
print(f'O menor número foi {min(listn)} e ele tava na posição: ', *listme)


val = [9, 4, 5, 0, 4, 6, 3, 2, 7, 10]

print(val)
val[4] = 1
print(val)
val.append(8)
print(val)
val.sort(reverse=True)
print(val)
val.pop()
print(val)
print(f'Valores: {len(val)}')
val.insert(5, 0)
print(val)
val.remove(0)
print(val)
for c,v in enumerate(val):
    print(f'Encontrei o número {v:2} na posição {c}.')

a = [7, 8, 0]
b = a
b[1] = 6
print(a, b)
b = a[:]
b[0] = 8
print(a, b)