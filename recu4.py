def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#pruebas
print(decimal_a_binario(0))   # "0" 
print(decimal_a_binario(1))   # "1" 
print(decimal_a_binario(2))   # "10" 
print(decimal_a_binario(5))   # "101" 
print(decimal_a_binario(10))  # "1010" 
print(decimal_a_binario(13))  # "1101" 


input("presione una tecla para continuar")