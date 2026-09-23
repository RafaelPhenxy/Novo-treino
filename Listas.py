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
print(f'O maior número foi {max(listn)} e ele tava na posição', *listm, sep= ', ')
print(f'O menor número foi {min(listn)} e ele tava na posição', *listme, sep= ', ')


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