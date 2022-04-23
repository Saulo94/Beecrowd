animal1 = input()
animal2 = input()
animal3 = input()

animais = {"vertebrado": {"ave": {"carnivoro": "aguia",
                                  "onivoro": "pomba"},
                          "mamifero": {"onivoro": "homem",
                                       "herbivoro": "vaca"}},
           "invertebrado": {"inseto": {"hematofago": "pulga",
                                       "herbivoro": "lagarta"},
                            "anelideo": {"hematofago": "sanguessuga",
                                         "onivoro": "minhoca"}}}

print(animais[animal1][animal2][animal3])
