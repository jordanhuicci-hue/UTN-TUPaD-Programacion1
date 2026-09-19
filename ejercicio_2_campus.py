usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada")
else:
    opcion = 0
    while opcion != 4:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_texto = input("Opción: ").strip()
        while not opcion_texto.isdigit() or not 1 <= int(opcion_texto) <= 4:
            if not opcion_texto.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion_texto = input("Opción: ").strip()
        opcion = int(opcion_texto)

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("Cada ejercicio que resolvés te ayuda a aprender.")
        else:
            print("Sesión finalizada.")

