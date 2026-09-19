# Cada turno se guarda en una variable propia; no se usan colecciones.
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: ingresá solo letras.")
    operador = input("Nombre del operador: ").strip()

opcion = 0
while opcion != 5:
    print("\n1) Reservar  2) Cancelar  3) Ver agenda  4) Resumen  5) Cerrar")
    opcion_texto = input("Opción: ").strip()
    while not opcion_texto.isdigit() or not 1 <= int(opcion_texto) <= 5:
        print("Error: elegí un número entre 1 y 5.")
        opcion_texto = input("Opción: ").strip()
    opcion = int(opcion_texto)

    if opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles")
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Empate en turnos ocupados")
    elif opcion == 5:
        print("Sistema cerrado.")
    else:
        dia_texto = input("Día (1=Lunes, 2=Martes): ").strip()
        while not dia_texto.isdigit() or (int(dia_texto) != 1 and int(dia_texto) != 2):
            print("Error: elegí 1 o 2.")
            dia_texto = input("Día (1=Lunes, 2=Martes): ").strip()
        dia = int(dia_texto)

        if dia == 1:
            turno1 = lunes1
            turno2 = lunes2
            turno3 = lunes3
            turno4 = lunes4
            cupos = 4
            nombre_dia = "Lunes"
        else:
            turno1 = martes1
            turno2 = martes2
            turno3 = martes3
            turno4 = ""
            cupos = 3
            nombre_dia = "Martes"

        if opcion == 3:
            print(f"Agenda del {nombre_dia}:")
            print(f"Turno 1: {turno1 if turno1 else '(libre)'}")
            print(f"Turno 2: {turno2 if turno2 else '(libre)'}")
            print(f"Turno 3: {turno3 if turno3 else '(libre)'}")
            if cupos == 4:
                print(f"Turno 4: {turno4 if turno4 else '(libre)'}")
        else:
            paciente = input("Nombre del paciente: ").strip()
            while not paciente.isalpha():
                print("Error: ingresá solo letras.")
                paciente = input("Nombre del paciente: ").strip()

            # Se comparan nombres sin distinguir mayúsculas de minúsculas.
            coincide1 = turno1.lower() == paciente.lower()
            coincide2 = turno2.lower() == paciente.lower()
            coincide3 = turno3.lower() == paciente.lower()
            coincide4 = cupos == 4 and turno4.lower() == paciente.lower()

            if opcion == 1:
                if coincide1 or coincide2 or coincide3 or coincide4:
                    print("Ese paciente ya tiene un turno en ese día.")
                elif turno1 == "":
                    turno1 = paciente
                    print("Turno 1 reservado.")
                elif turno2 == "":
                    turno2 = paciente
                    print("Turno 2 reservado.")
                elif turno3 == "":
                    turno3 = paciente
                    print("Turno 3 reservado.")
                elif cupos == 4 and turno4 == "":
                    turno4 = paciente
                    print("Turno 4 reservado.")
                else:
                    print("No quedan cupos para ese día.")
            elif opcion == 2:
                if coincide1:
                    turno1 = ""
                    print("Turno cancelado.")
                elif coincide2:
                    turno2 = ""
                    print("Turno cancelado.")
                elif coincide3:
                    turno3 = ""
                    print("Turno cancelado.")
                elif coincide4:
                    turno4 = ""
                    print("Turno cancelado.")
                else:
                    print("No se encontró ese paciente en el día elegido.")

        # Copiar al día elegido las posibles modificaciones.
        if dia == 1:
            lunes1 = turno1
            lunes2 = turno2
            lunes3 = turno3
            lunes4 = turno4
        else:
            martes1 = turno1
            martes2 = turno2
            martes3 = turno3

