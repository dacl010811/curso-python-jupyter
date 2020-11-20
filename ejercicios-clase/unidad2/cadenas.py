from colorama import Style, Fore

cadena_simple = 'Esta'
cadena_dos = "Hola Python\n"

# Comentarios
c = cadena_dos + cadena_simple 
print(type(len(cadena_simple)))
d = cadena_dos * len(cadena_simple) #4 (int)
print(type(d))
#print("El resultado de la concatenacion es : \n"+c)
print(f"El resultado :\n{Fore.GREEN}{d}{Style.RESET_ALL}")

