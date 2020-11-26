
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



if __name__ == "__main__":
    total_factura = facturacion(1000)
    print ("El valor total 1  es = ",total_factura)

    total_factura = facturacion(1000,10)  # Invocacion de la funcion modificando el iva  respecto al valor por defecto
    print ("El valor total 2 es = ",total_factura)


