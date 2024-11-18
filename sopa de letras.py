# Definición de la sopa de letras como una lista de listas
letter_soup = [
    ["A", "M", "A", "R", "S"],
    ["S", "T", "E", "R", "I"],
    ["O", "M", "A", "Z", "C"],
    ["A", "L", "C", "R", "H"],
    ["P", "O", "L", "O", "S"]
]

# Nueva lista de palabras a buscar en la sopa de letras
words_to_find = ["MAR", "SOL", "AMOR", "AL", "ROSA", "CERO", "RICO", "SER", "SAL", "CASA"]

# Función para chequear si una palabra está en la sopa de letras en forma horizontal o vertical
def find_word(letter_soup, word):
    # Convertir cada fila en una cadena para búsqueda horizontal
    for row in letter_soup:
        if word in ''.join(row):
            return True
    
    # Convertir cada columna en una cadena para búsqueda vertical
    for col in range(len(letter_soup[0])):
        column = ''.join([letter_soup[row][col] for row in range(len(letter_soup))])
        if word in column:
            return True

    return False

# Generar el reporte de palabras encontradas
report = {word: find_word(letter_soup, word) for word in words_to_find}

# Imprimir el reporte
print(report)