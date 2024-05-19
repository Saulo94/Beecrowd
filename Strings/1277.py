n_casos = int(input())

for _ in range(n_casos):
    n_estudantes = int(input())

    estudantes_faltantes = []

    estudantes = input().split()

    frequencias = input().split()

    for i, frequencia in enumerate(frequencias):

        # pct_faltas = A / (A + P)

        count_ausencias = frequencia.count("A")

        count_presencas = frequencia.count("P")

        if count_ausencias / (count_presencas + count_ausencias) > 0.25:
            estudantes_faltantes.append(estudantes[i])
    
    print(" ".join(estudantes_faltantes))
