# Función para calcular el descuento
#se trata de que de el programa tome dos parametros el valor total de la compra y el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # lista  con productos y sus precios
    productos = {
        "Manzanas": 2.00,  # Precio por kilo
        "Leche": 1.00,  # Precio por litro
        "Pan": 0.20,  # Precio por unidad
        "Arroz": 0.50,  # Precio por libra
        "Huevos": 3.85  # Precio por cubeta
    }

    # Primera llamada a la función (por defecto 10% de descuento)
    producto_1 = "Manzanas"
    cantidad_1 = 3  # 3 kilos de manzanas
    monto_total_1 = productos[producto_1] * cantidad_1
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(
        f"Compra de {cantidad_1} kg de {producto_1}: Monto Total: ${monto_total_1:.2f}, Descuento: ${descuento_1:.2f}, Monto Final: ${monto_final_1:.2f}")

    # Segunda llamada a la función proporcionando un porcentaje de descuento diferente
    producto_2 = "Leche"
    cantidad_2 = 4  # 4 litros de leche
    porcentaje_descuento_2 = 15
    monto_total_2 = productos[producto_2] * cantidad_2
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(
        f"Compra de {cantidad_2} litros de {producto_2}: Monto Total: ${monto_total_2:.2f}, Descuento: ${descuento_2:.2f}, Monto Final: ${monto_final_2:.2f}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()

