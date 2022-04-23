n1, n2, n3, n4 = map(float, input().split())
media = ((2 * n1) + (3 * n2) + (4 * n3) + n4) / 10

print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: {:.1f}".format(ne))

    mediaf = round((ne + media) / 2, 1)
    if mediaf >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(mediaf))
