import string
import random

# Definición de la función que genera contraseñas
def generar_contrasena(tamano, usar_mayusculas=True, usar_minusculas=True, usar_digitos=True, usar_especiales=True):
    # Inicialización de la variable que contendrá los caracteres posibles
    caracteres = ""
    
    # Construcción de la lista de caracteres posibles según las preferencias del usuario
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation
    
    # Verificación de que al menos se haya permitido un tipo de caracteres
    if not caracteres:
        print("Error: Debes permitir al menos un tipo de caracteres.")
        return None
    
    # Generación de la contraseña aleatoria
    contrasena = "".join(random.choice(caracteres) for _ in range(tamano))
    return contrasena

# Función principal del programa
def main():
    # Solicitar al usuario el tamaño de la contraseña
    tamano = int(input("Ingrese el tamaño de la contraseña: "))
    
    # Solicitar al usuario sus preferencias sobre el tipo de caracteres a incluir
    usar_mayusculas = input("¿Permitir mayúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("¿Permitir minúsculas? (s/n): ").lower() == 's'
    usar_digitos = input("¿Permitir dígitos? (s/n): ").lower() == 's'
    usar_especiales = input("¿Permitir caracteres especiales? (s/n): ").lower() == 's'
    
    # Llamada a la función para generar la contraseña
    contrasena = generar_contrasena(tamano, usar_mayusculas, usar_minusculas, usar_digitos, usar_especiales)
    
    # Imprimir la contraseña generada si la función la devuelve
    if contrasena:
        print("La contraseña generada es:", contrasena)

# Comprobar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Llamada a la función principal
    main()
