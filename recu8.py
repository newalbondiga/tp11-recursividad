def contar_digito(numero, digito):
   
    
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El 'numero' debe ser un entero positivo.")
    if not isinstance(digito, int) or not (0 <= digito <= 9):
        raise ValueError("El 'digito' debe ser un entero entre 0 y 9.")

  
    if numero == 0:
        return 0

   
    ultimo_digito = numero % 10
   
    numero_sin_ultimo_digito = numero // 10
    
  
    conteo_actual = 0
    if ultimo_digito == digito:
        conteo_actual = 1
    
   
    return conteo_actual + contar_digito(numero_sin_ultimo_digito, digito)

#ejemplos
print("--- Contador de Dígitos Recursivo ---")

# Ejemplos proporcionados:
print(f"contar_digito(12233421, 2) → {contar_digito(12233421, 2)}")
print(f"contar_digito(5555, 5) → {contar_digito(5555, 5)}")         
print(f"contar_digito(123456, 7) → {contar_digito(123456, 7)}")     

print("-" * 40)

#ejemplos:
print(f"contar_digito(100100, 0) → {contar_digito(100100, 0)}")    
print(f"contar_digito(1, 1) → {contar_digito(1, 1)}")               
print(f"contar_digito(123, 4) → {contar_digito(123, 4)}")          
print(f"contar_digito(0, 0) → {contar_digito(0, 0)}")               

print("-" * 40)

# Prueba
while True:
    try:
        entrada_numero = input("Ingresa un número entero positivo (o 'salir' para terminar): ")
        if entrada_numero.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        num = int(entrada_numero)

        entrada_digito = input("Ingresa el dígito a buscar (0-9): ")
        dig = int(entrada_digito)
        
        if num < 0:
            print("Error: El número debe ser positivo.")
        elif not (0 <= dig <= 9):
            print("Error: El dígito a buscar debe estar entre 0 y 9.")
        else:
            resultado_conteo = contar_digito(num, dig)
            print(f"El dígito {dig} aparece {resultado_conteo} veces en el número {num}.")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingresa números enteros.")
    except RecursionError:
        print("Error: La recursión ha excedido el límite. El número podría ser demasiado grande.")
    print("-" * 40)
    
    
    input("presione una tecla para continuar")