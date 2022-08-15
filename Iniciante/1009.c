#include <stdio.h>

int main(){
  double salario, vendas;
  scanf("%s");
  scanf("%lf", &salario);
  scanf("%lf", & vendas);
  salario = salario + vendas * 0.15;
  printf("TOTAL = R$ %.2lf\n", salario);
  return 0;
}
