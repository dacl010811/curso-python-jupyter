
num_elementos = int (input("Cuantos numeros desea ingresar\n"))
suma = 0

for numero in range(num_elementos):
    suma += float (input("Ingresa un numero : \n"))

print ("Se han ingresado {} numeros, que la media aritmetica es = {}".format(num_elementos, suma/num_elementos))


