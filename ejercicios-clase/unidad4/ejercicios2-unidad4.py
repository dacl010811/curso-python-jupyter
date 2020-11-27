import math

"""
    Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
    La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
    y devolver el total de la factura. 
    
    Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

    """

#Iva por defecto sea = 12%

def facturacion(total, iva=21):
    """Realiza el calculo de la facturacion
    Args:
        total (float): Total de la factura sin impuesto
        iva (float): IVA. Defaults to 21.
    Returns:
        [float]: Total de la factura
    """
    return total + total*iva/100 


    """
    Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
    """

    """  [2,3,45,5,n]
         resultado : [2**2,3**2,45**2,5**2,n**2] 
    """  
    
def  cuadrado(*args):
    lista_cuadrados = []
    if args:
        for numero in args:
            print("N:",numero)
            lista_cuadrados.append(numero**2)
    return lista_cuadrados


def teclado():
    lista_numeros = []
    contador = 0
    while True: 
        try: 
            numero = input ("Ingresa  el numero [{0}]: \n".format(contador))
            lista_numeros.append(int(numero))
            contador +=1
            respuesta = input ("Desea continuar ingresando mas datos, y/n \n")
            if respuesta.upper() == 'N':
                    break
        except ValueError as ve:
            print("Error ValueError Controlado :",ve.__class__)
        except Exception as e:
            print("EL error encontrado es : ", e.__class__)        
    
    return  lista_numeros 


if __name__ == "__main__":
   
    resultado_lista = cuadrado(*teclado())
    print(" La lista de cuadrados es = {0}".format(resultado_lista))


