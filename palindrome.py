def is_palindrome(s: str) -> bool:
    # Convertimos la cadena a minúsculas y eliminamos los caracteres que no son alfanuméricos
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Inicializamos dos punteros
    left, right = 0, len(s) - 1
    
    # Mientras los dos punteros no se crucen
    while left < right:
        # Si los caracteres en ambos punteros no coinciden, no es palíndromo
        if s[left] != s[right]:
            return False
        # Movemos los punteros
        left += 1
        right -= 1
    
    # Si completamos el ciclo sin encontrar diferencias, es palíndromo
    return True

print(is_palindrome("ana"))