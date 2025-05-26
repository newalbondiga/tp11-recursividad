def es_palindromo(palabra):
    
    #si la palabra tiene 0 o 1 caracter es un palíndromo.
  
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo:
    # Si el primer y el último caracter son iguales,

    if palabra[0] == palabra[len(palabra) - 1]:
        return es_palindromo(palabra[1 : len(palabra) - 1])
    else:
        # Si el primer y el último caracter no son iguales, no es un palíndromo.
        return False

#ejemplos
print("--- Verificador de Palíndromos Recursivo ---")


print(f"'reconocer' es palíndromo? {es_palindromo('reconocer')}") 
print(f"'anna' es palíndromo? {es_palindromo('anna')}")           
print(f"'oso' es palíndromo? {es_palindromo('oso')}")             
print(f"'a' es palíndromo? {es_palindromo('a')}")                 
print(f"'' (vacío) es palíndromo? {es_palindromo('')}")           

print("-" * 30)

# No palíndromos
print(f"'python' es palíndromo? {es_palindromo('python')}")       
print(f"'casa' es palíndromo? {es_palindromo('casa')}")           
print(f"'anilina' es palíndromo? {es_palindromo('anilina')}")     

print("-" * 30)

# Prueba
while True:
    entrada = input("Ingresa una palabra (sin espacios ni tildes, o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        print("Saliendo del programa.")
        break
    
    # Opcional: limpiar la entrada para asegurar que no tenga espacios ni tildes
    
    entrada_limpia = entrada.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

    if es_palindromo(entrada_limpia):
        print(f"'{entrada}' SÍ es un palíndromo.")
    else:
        print(f"'{entrada}' NO es un palíndromo.")
    print("-" * 30)

input("presione una tecla para continuar")