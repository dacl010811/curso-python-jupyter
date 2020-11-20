# Sacar  la nota promedio por porcentaje

nota_1 = 10.0 # 15%
nota_2 = 8.5  # 35%
nota_3 = 8    # 50%

promedio = ((nota_1*0.15)+(nota_1*0.35)+(nota_1*0.50))/3

print(type(promedio))

print("El resultado es : {}".format(round(promedio,3)))