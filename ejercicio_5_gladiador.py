print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True
juego_activo = True

print("=== INICIO DEL COMBATE ===")
while juego_activo and vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("1) Ataque Pesado  2) Ráfaga Veloz  3) Curar")
        opcion_texto = input("Opción: ").strip()
        while not opcion_texto.isdigit() or not 1 <= int(opcion_texto) <= 3:
            print("Error: Ingrese un número del 1 al 3.")
            opcion_texto = input("Opción: ").strip()
        opcion = int(opcion_texto)

        if opcion == 1:
            danio = float(ataque_pesado)
            if vida_enemigo < 20:
                danio = ataque_pesado * 1.5
                print("¡Golpe crítico!")
            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio:g} puntos de daño!")
        elif opcion == 2:
            print("¡Inicias una ráfaga de golpes!")
            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
        else:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Recuperaste 30 puntos de vida.")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False
    else:
        # Un enemigo derrotado no llega a ejecutar otro turno.
        vida_jugador -= ataque_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador = True

    if vida_jugador <= 0 or vida_enemigo <= 0:
        juego_activo = False

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

