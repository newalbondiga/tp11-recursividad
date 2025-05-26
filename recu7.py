def contar_bloques(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return n + contar_bloques(n - 1)

#Ejemplos
print("--- Calculadora de Bloques de Pirámide Recursiva ---")

 
print(f"Para n = 1: {contar_bloques(1)} bloques") 
print(f"Para n = 2: {contar_bloques(2)} bloques") 
print(f"Para n = 4: {contar_bloques(4)} bloques") 

print("-" * 40)


print(f"Para n = 5: {contar_bloques(5)} bloques") 
print(f"Para n = 0: {contar_bloques(0)} bloques") 
print(f"Para n = 10: {contar_bloques(10)} bloques") 

print("-" * 40)

# Prueba
while True:
    try:
        entrada_usuario = input("Ingresa el número de bloques en el nivel más bajo (n, o 'salir' para terminar): ")
        if entrada_usuario.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        n_bloques = int(entrada_usuario)
        
        if n_bloques < 0:
            print("Por favor, ingresa un número entero no negativo para los bloques del nivel más bajo.")
        else:
            total_bloques = contar_bloques(n_bloques)
            print(f"Para una pirámide con {n_bloques} bloques en la base, se necesitan {total_bloques} bloques en total.")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
    except RecursionError:
        print("Error: La recursión ha excedido el límite. El número podría ser demasiado grande.")
    print("-" * 40)
    
    
    
    input("presione una tecla para continuar")