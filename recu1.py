def factorial_recursivo(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

#pidiendo entero
try:
    num_usuario = int(input("Ingresa un número entero positivo: "))

    if num_usuario < 0:
        print("ingresa un número no negativo.")
    else:
        print(f"Calculando factoriales del 1 al {num_usuario}:")
        for i in range(1, num_usuario + 1):
            print(f"El factorial de {i} es: {factorial_recursivo(i)}")
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")
    
    


input("presione una tecla para continuar")