nombre = input("Nombre del cliente: ").strip()
while not nombre.isalpha():
    print("Error: ingresá un nombre que contenga solo letras.")
    nombre = input("Nombre del cliente: ").strip()

cantidad_texto = input("Cantidad de productos: ").strip()
while not cantidad_texto.isdigit() or int(cantidad_texto) == 0:
    print("Error: ingresá un número entero positivo.")
    cantidad_texto = input("Cantidad de productos: ").strip()
cantidad = int(cantidad_texto)

total_sin_descuentos = 0
total_con_descuentos = 0.0

for producto in range(1, cantidad + 1):
    precio_texto = input(f"Producto {producto} - Precio: ").strip()
    while not precio_texto.isdigit():
        print("Error: ingresá un precio entero no negativo.")
        precio_texto = input(f"Producto {producto} - Precio: ").strip()
    precio = int(precio_texto)

    descuento = input("Descuento (S/N): ").strip().lower()
    while descuento != "s" and descuento != "n":
        print("Error: respondé S o N.")
        descuento = input("Descuento (S/N): ").strip().lower()

    total_sin_descuentos += precio
    if descuento == "s":
        total_con_descuentos += precio * 0.90
    else:
        total_con_descuentos += precio

ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad

print(f"\nCliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

