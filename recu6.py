def suma_digitos(n):
   
    # Caso base: Si el número es 0, la suma de sus dígitos es 0.
    if n == 0:
        return 0
    # Caso para números negativos 
    elif n < 0:
        
        return suma_digitos(abs(n)) 
    
    #
    # n // 10 nos da el número sin su último dígito (división entera).
    return (n % 10) + suma_digitos(n // 10)

# --- Ejemplos de uso ---
print("--- Suma de Dígitos Recursiva ---")

print(f"La suma de los dígitos de 1234 es: {suma_digitos(1234)}") 
print(f"La suma de los dígitos de 9 es: {suma_digitos(9)}")     
print(f"La suma de los dígitos de 305 es: {suma_digitos(305)}")  
print(f"La suma de los dígitos de 0 es: {suma_digitos(0)}")
print(f"La suma de los dígitos de 7890 es: {suma_digitos(7890)}")
print(f"La suma de los dígitos de 100000 es: {suma_digitos(100000)}")

print("-" * 40)

# Prueba
while True:
    try:
        entrada_usuario = input("Ingresa un número entero positivo (o 'salir' para terminar): ")
        if entrada_usuario.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        num_entero = int(entrada_usuario)
        
        if num_entero < 0:
            print("Por favor, ingresa un número entero positivo.")
        else:
            resultado_suma = suma_digitos(num_entero)
            print(f"La suma de los dígitos de {num_entero} es: {resultado_suma}")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
    except RecursionError:
        print("Error: La recursión ha excedido el límite. El número podría ser demasiado grande.")
    print("-" * 40)
    
    
    input("presione una tecla para continuar")