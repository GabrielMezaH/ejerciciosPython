precios = {
    (1, 20): 30,
    (21, 41): 28,
    (42, 62): 26.5,
    (63, 83): 24.5
}

def calcular_importe_compra(cantidad):
    for rango, precio in precios.items():
        min_unidades, max_unidades = rango
        if min_unidades <= cantidad <= max_unidades:
            importe = cantidad * precio
            return importe

# Función para calcular el descuento
def calcular_descuento(cantidad, importe_compra):
    if cantidad > 41:
        descuento = 0.15 * importe_compra
    else:
        descuento = 0.05 * importe_compra
    return descuento

# Función principal
def main():
    cantidad = int(input("Ingrese la cantidad de unidades a comprar: "))
    importe_compra = calcular_importe_compra(cantidad)
    descuento = calcular_descuento(cantidad, importe_compra)
    importe_a_pagar = importe_compra - descuento

    print(f"Importe de la compra: S/. {importe_compra:.2f}")
    print(f"Descuento aplicado: S/. {descuento:.2f}")
    print(f"Importe a pagar: S/. {importe_a_pagar:.2f}")

if __name__ == "__main__":
    main()