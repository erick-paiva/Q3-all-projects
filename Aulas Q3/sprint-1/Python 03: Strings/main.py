# # Utilizando ' entre ""
# minha_string = "Estou em Marthas's Vineyard, na Virginia."
# minha_string
# "Estou em Marthas's Vineyard, na Virginia."

# # Utilizando / para escapar aspas ' dentro da string ''
# minha_string = 'Estou em Martha\'s Vineyard, na Virgínia.'
# minha_string
# "Estou em Marthas's Vineyard, na Virginia."

# # Utilizando aspas triplas (Strings com multiplas linhas)
# minha_string = """ Lorem ipsum dolor sit, amet consectetur adipisicing
#  elit. Porro, ad mollitia labore laborum debitis quas distinctio, eveniet
#  excepturi adipisci culpa ab voluptatum! Natus placeat voluptatibus rerum
#  reiciendis magni autem ratione. """
 
# nome = 'Lucas'

# # Acessando índice da string
# nome[0]
# 'L'
# # Acessando o último caracter de uma string
# nome[-1]
# 's'

# print(nome[-1])

# # Fatiamento ou slicing
# nome = 'Lucas'

# # Acessando os índices do 0 ao 2 (0 incluso, 2 não incluso)
# nome[:2]
# 'Lu'
# # Acessando os índices do 2 até o fim da string
# nome[2:]
# 'cas'

# # Acessando do 1 ao 4, com passo 2 (1 incluso, 4 não incluso)
# nome[1:4:2]
# 'ua'

# print(len(nome), "interessante")
# # print(1 == 1)
# def are_you_playing_banjo(name):
#     # Implement me!
#     result = name[0].lower()
#     print(result)
#     if result == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"
        
# # return f"{name} plays banjo" if result == "r" else return f"{name} does not play banjo"


# print(are_you_playing_banjo("Eick"))



# def reverse_words(s):
#     # result = 
#     # result.reverse()
#     print(s.split())

#     # result = " ".join(result)
#     # print(result)
#     # return result
# reverse_words("erick")
# result = "".join(["a","b","c"])
# result = [1,2,3,4]
# result.reverse()
# result = "abc"
# result = list(result)
# result.reverse()
# # result.reverse()
# # print(result)
# test = ["a","b","c"]
# test2 = reversed(test)
# print(test2)
# for string
# seq_string = 'Python'
# print(list(reversed(seq_string)))

# # for tuple
# seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# print(list(reversed(seq_tuple)))

# # for range
# seq_range = range(5, 9)
# print(list(reversed(seq_range)))

# # for list
# seq_list = [1, 2, 4, 3, 5]
# print(list(reversed(seq_list)))
# print(len("aaa"))
# arr = [1,2,3]
# for arr in range(4):
def accum(s):
    resultado = []
    for i in range(len(s)):
        resultado.append(s[i].upper() + s[i].lower() * i)
    return "-".join(resultado)
print(accum("EvidjUnokmM"))