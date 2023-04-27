# cifrado cesar funcion
def cifrar_cesar(mensaje, n): 
    resultado = "" 
    for i in range(len(mensaje)): 
        char = mensaje[i] 
        # si el caracter es una letra mayúscula 
        if (char.isupper()): 
            resultado += chr((ord(char) + n-65) % 26 + 65) 
        # si el caracter es una letra minúscula 
        else: 
            resultado += chr((ord(char) + n - 97) % 26 + 97) 
  
    return resultado 

# descrifrado cesar funcion
def decifrar_cesar(texto, deslocamento):
    decifrado = ''

    for letra in texto:
        if letra.isalpha():
            num = ord(letra) - deslocamento

            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26

            decifrado += chr(num)
        else:
            decifrado += letra

    return decifrado


# Prueba
mensaje = "hola"
n = 14
cifrado = cifrar_cesar(mensaje, n)

print("Mensaje: ", mensaje) 
print("Mensaje cifrado: ", cifrado)
print("Mensaje decifrado: ", decifrar_cesar(cifrado, n))


"""
Output console: 
                Mensaje:  hola
                Mensaje cifrado:  vczo
                Mensaje decifrado:  hola
"""