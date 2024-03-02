def validar_edad(edad):
    if 0 <= edad <= 120:  # Suponemos que las edades válidas están en el rango de 0 a 120 años
        print("La edad es válida.")
    else:
        print("La edad no está en el rango permitido (0-120).")

# Ejemplo de uso
try:
    edad = int(input("Ingrese la edad del usuario: "))
    validar_edad(edad)
except ValueError:
    print("Ingrese un valor numérico para la edad.")


