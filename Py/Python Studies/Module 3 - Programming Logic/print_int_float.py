"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Ivan Campaneli')
print(1, 'Ivan "Campaneli"')

# Aspas duplas
print("Ivan Campaneli")
print(2, "Ivan 'Campaneli'")

# Escape
print("Ivan \"Campaneli\"")

# r
print(r"Ivan \"Campaneli\"")

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
# print(11) # int
# print(-11) # int
# print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
# print(1.1, 10.11)
# print(0.0, -1.5)

# A função type mostra o tipo que o Python
# inferiu ao valor.

print(type('Ivan'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))