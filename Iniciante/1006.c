#include <stdio.h>

int main(){
  double nota1, nota2, nota3, media;
  scanf("%lf", &nota1);
  scanf("%lf", &nota2);
  scanf("%lf", &nota3);

  media = (nota1 * 0.2 + nota2 * 0.3 + nota3 * 0.5);
  printf("MEDIA = %.1lf\n", media);
  return 0;
}
