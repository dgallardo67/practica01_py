lista1 = [1, 2, 5, 8, 23, 52]

for i in lista1:
    print(i)

lista1.append(24)

print(lista1)

lista1.remove(5)
print(lista1)

lista1.insert(1,86)
print(lista1)

lista1.pop()
print(lista1)

lista1.reverse()
print(lista1)

lista1.sort()
print(lista1)


lista2 = [4, 8, 19, [30, 90,80]]
for x in range(len(lista2)):
    if(x == 3):
        for y in range(len(lista2[x])):
            print(lista2[x][y])
    else:
        print(lista2[x])




