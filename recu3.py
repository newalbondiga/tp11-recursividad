def potencia_recursiva(base, exponente):
   
   
  
    if exponente == 0:
        return 1
    # Caso base para exponente negativo (opcional, pero buena práctica)
   
    elif exponente < 0:
        print("Advertencia: Esta implementación de potencia_recursiva no maneja exponentes negativos correctamente.")
        return 1 / potencia_recursiva(base, abs(exponente))
    
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Algoritmo general para probar la función

print("--- Calculadora de Potencias Recursiva ---")

while True:
    try:
        entrada_base = input("Ingresa la base (o 'salir' para terminar): ")
        if entrada_base.lower() == 'salir':
            print("Saliendo del programa.")
            break
        base = float(entrada_base)

        entrada_exponente = input("Ingresa el exponente (entero no negativo): ")
        exponente = int(entrada_exponente)

        if exponente < 0:
            print("Error: Por favor, ingresa un exponente no negativo para esta función recursiva simple.")
            continue

        resultado = potencia_recursiva(base, exponente)
        print(f"{base} elevado a la {exponente} es: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, asegúrate de ingresar números válidos.")
    except RecursionError:
        print("Error: La recursión ha excedido el límite. Esto podría ocurrir con exponentes muy grandes.")
    print("-" * 30)



input("presione una tecla para continuar")