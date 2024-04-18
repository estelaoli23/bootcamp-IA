nome = "Estelinha"
idade = 31
profissao = "Analista de Sistemas"
linguagem = "Python"

# porcentagem s. de string, de acordo com o caracter da varivavel - na idadei usei %d, de decimal, ou int, acabou caindo em desuso pelo tamanho, tem uma forma mais facil, que será mostrada na próxima lição
print("Olá meu nome é %s, tenho %d anos de idade, trabalho como %s, e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))


# interpolação de strings, é  a forma mais limpa de fazer esse método
print(f"Olá meu nome é {nome}, tenho {idade} anos de idade, trabalho como {profissao}, e estou matriculada no curso de {linguagem}.")

PI = 3.14159
# f de float
print(f"Valor de PI: {PI: .2f}")


