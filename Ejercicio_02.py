# DELACRACIÓN DE VARIABLES
goles_a = 0
goles_b = 0
mensaje = ""

# ENTRADA
goles_a = int(input("Ingrese goles de A: "))
goles_b = int(input("Ingrese goles de B: "))

# PROCESO
if goles_a>goles_b:
    mensaje = "Ganó A !!"
else:
    if goles_a<goles_b:
        mensaje = "Ganó B !!"
    else:
        mensaje = "Empate !!"

# SALIDA
print(mensaje)