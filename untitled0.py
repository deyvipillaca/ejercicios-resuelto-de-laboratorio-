def validar_edad():
    while True:
        edad = int(input("Por favor, ingrese su edad: "))
        if 1 <= edad <= 120:
            print("Edad válida:", edad)
            break
        else:
            print("La edad ingresada no está dentro del rango permitido (1-120). Inténtelo de nuevo.")

# Llamar a la función para validar la edad del usuario
validar_edad()
