#include <stdio.h>

int main(){
  int numero, horas;
  double salario;
  scanf("%d", &numero);
  scanf("%d", &horas);
  scanf("%lf", &salario);
  printf("NUMBER = %d\n", numero);
  printf("SALARY = U$ %.2lf\n", horas * salario);

  return 0;
}
