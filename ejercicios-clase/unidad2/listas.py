


matriz = [
    [1, 1, 1, 3], #0
    [2, 2, 2, 7], #1
    [3, 3, 3, 9], #2
    [4, 4, 4, 13] #3
]

#print(type(matriz))
#print(len(matriz))
#print(matriz)
a = sum([8,3,4])
print(a)

"""matriz[1][-1] = sum(matriz[1][:3])
matriz[3][-1] = sum(matriz[3][:-1])"""

print (matriz[0][0])

matriz[0][0] = sum(matriz[0][-3:])
matriz[1][0] = sum(matriz[1][-3:])
matriz[2][0] = sum(matriz[2][-3:])
matriz[3][0] = sum(matriz[3][-3:])


print(matriz)
