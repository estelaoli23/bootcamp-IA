curso = "pYtHon"

# maiucuslo
print(curso.upper())
# minusculo
print(curso.lower())
# prim letra maiuscula
print(curso.title())

# remove espaço na esq e dir
print(curso.strip())
# remove o espaco esq
print(curso.lstrip())
# remove o espaco dir
print(curso.rstrip())

# centraliza, vc coloca o numero de caracteres, o 2 argumento é opcional, se nao informar, vai ser em branco
print(curso.center(10, "#"))
# junção do caracter "." na string, faz um for na palavra e coloca o caractere
print(".".join(curso))

