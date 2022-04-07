dic_altternativas = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

qt_teste = int(input())
while qt_teste:
    for _ in range(qt_teste):
        """alternativa_marcada = len([int(alternativa) for index, alternativa in enumerate(input().split())
                                   if int(alternativa) <= 127])"""
        alternativa_marcada = [index for index, alternativa in enumerate(input().split())
                               if int(alternativa) <= 127]
        if len(alternativa_marcada) == 1:
            print(dic_altternativas[alternativa_marcada[0]])
        else:
            print('*')
    qt_teste = int(input())
