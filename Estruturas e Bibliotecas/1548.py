quat_teste = int(input())
for _ in range(quat_teste):
    input()
    alunos = list(map(int, input().split()))

    quat_igual = 0
    for i, aluno in enumerate(sorted(alunos, reverse=True)):
        if alunos[i] == aluno:
            quat_igual += 1
    print(quat_igual)
