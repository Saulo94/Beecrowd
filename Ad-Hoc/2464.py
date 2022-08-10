chave = input()

dicionario = {chave[letra]: chr(letra + 97) 
              for letra in range(26)}

frase = input()

palavra_final = "".join([dicionario[letra] 
                        for letra in frase])

print(palavra_final)
