list_ddd = {"21": "Rio de Janeiro",
            "61": "Brasilia",
            "71": "Salvador",
            "11": "Sao Paulo",
            "32": "Juiz de Fora",
            "19": "Campinas",
            "27": "Vitoria",
            "31": "Belo Horizonte"}

number_ddd = input()

if number_ddd in list_ddd:
    print(list_ddd[number_ddd])
else:
    print("DDD nao cadastrado")
