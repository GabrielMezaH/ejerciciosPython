# DELACRACIÓN DE VARIABLES
nota = 0
ponderado = 0
categoria = ""

# ENTRADA
nota = float(input("Ingrese ponderado: "))

# PROCESO
if 16 <= nota <= 20:
    categoria = "A"
elif 12 <= nota < 16:
    categoria = "B"
elif 10 <= nota < 12:
    categoria = "C"
else:
    categoria = "D"

# SALIDA
print("categoria: " , categoria)