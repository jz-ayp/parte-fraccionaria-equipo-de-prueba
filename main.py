
"""
Determinar si un número tiene parte fraccionaria
"""

# Entradas
numero = eval(input("Introduzca un número: "))
	
# Proceso
if numero == int(numero):
	resultado = "No"
else:
	resultado = "Sí"

# Salidas
print(resultado, "tiene decimales")

