nombre = input("Nombre del agente: ").strip()
while not nombre.isalpha():
    print("Error: ingresá solo letras.")
    nombre = input("Nombre del agente: ").strip()

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0

print(f"Bienvenido a la bóveda, {nombre}.")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion_texto = input("Opción: ").strip()
    while not opcion_texto.isdigit() or not 1 <= int(opcion_texto) <= 3:
        print("Error: elegí 1, 2 o 3.")
        opcion_texto = input("Opción: ").strip()
    opcion = int(opcion_texto)

    if opcion == 1:
        # El riesgo se evalúa con la energía que había al elegir la acción.
        riesgo = energia < 40
        forzadas_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzadas_seguidas == 3:
            alarma = True
            print("La cerradura se trabó: tercera fuerza seguida. ¡Alarma activada!")
        else:
            if riesgo:
                numero_texto = input("Riesgo de alarma: elegí un número del 1 al 3: ").strip()
                while not numero_texto.isdigit() or not 1 <= int(numero_texto) <= 3:
                    print("Error: elegí 1, 2 o 3.")
                    numero_texto = input("Número del 1 al 3: ").strip()
                if int(numero_texto) == 3:
                    alarma = True
                    print("¡Alarma activada!")
            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

    elif opcion == 2:
        forzadas_seguidas = 0
        energia -= 10
        tiempo -= 3
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Hackeo, paso {paso}/4. Código: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El código abrió una cerradura.")

    else:
        forzadas_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
        print("Descansaste.")

print("\nFin del juego")
if energia <= 0 or tiempo <= 0:
    print("DERROTA: se agotó la energía o el tiempo.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA: bloqueo por alarma.")
elif cerraduras_abiertas == 3:
    print(f"VICTORIA, {nombre}: abriste la bóveda.")

