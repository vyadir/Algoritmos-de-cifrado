def cifra_vigenere(text, key): 
    cipher_text = "" 
    # recorrer los caracteres individualmente 
    for i in range(len(text)): 
        char = text[i] 
        # Si el caracter no es una letra de alfabeto, no se cifra
        if (char.isalpha()): 
            # Obtener el codigo ASCII
            code_ASCII = ord(char) 
            # Aplicar la clave
            code_ASCII += ord(key[i % len(key)]) - 97
            # Si se desborda, empezar desde el principio
            if code_ASCII > ord('z'): 
                code_ASCII -= 26
            # Agregar el caracter cifrado al texto cifrado
            cipher_text += chr(code_ASCII) 
        else: 
            # Si no es una letra, agregar tal cual 
            cipher_text += char 
    return cipher_text 

#Codigo para el decifrado de Vigenere
def decifra_vigenere(cipher_text, key): 
    plain_text = "" 
    # recorrer los caracteres individualmente 
    for i in range(len(cipher_text)): 
        char = cipher_text[i] 
        # Si el caracter no es una letra de alfabeto, no se cifra
        if (char.isalpha()): 
            # Obtener el codigo ASCII
            code_ASCII = ord(char) 
            # Aplicar la clave
            code_ASCII -= ord(key[i % len(key)]) - 97
            # Si se desborda, ir al final
            if code_ASCII < ord('a'): 
                code_ASCII += 26
            # Agregar el caracter cifrado al texto cifrado
            plain_text += chr(code_ASCII) 
        else: 
            # Si no es una letra, agregar tal cual 
            plain_text += char 
    return plain_text

#---------------------------------------------Ejemplo
string = 'hola mundo'
key = 'secreto'

encriptado = cifra_vigenere(string, key)
decifrado = decifra_vigenere(encriptado,key)
print(encriptado)
print(decifrado)



"""
Output:
         zsnr fifhq
         hola mundo
"""