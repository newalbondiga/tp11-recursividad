def fibonacci_recursivo(pos):
    
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
       
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

#posición hasta la que desea ver la serie
try:
    limite_pos = int(input("Ingresa un nmero entero no negativo para la serie de Fibonacci: "))

    if limite_pos < 0:
        print("ingresa un número no negativo para la posisción.")
    else:
        print(f"\nSerie de Fibonacci hasta la posición {limite_pos}:")
        serie_completa = []
        for i in range(limite_pos + 1):
            valor_fib = fibonacci_recursivo(i)
            serie_completa.append(valor_fib)
        print(serie_completa)

except ValueError:
    print("ingresa un número entero.")


input("presione una tecla para continuar")