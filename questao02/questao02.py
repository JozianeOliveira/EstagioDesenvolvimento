# Verificar a Existência da Letra 'a' em uma String

def count_a_in_string(string):
    count = string.lower().count('a')
    return count

# String a ser analisada
texto = input("Informe uma string: ")

# Contando as ocorrências de 'a'
qtd_a = count_a_in_string(texto)
print(f"A letra 'a' aparece {qtd_a} vezes na string.")
