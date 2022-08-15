#include <stdio.h>

int main(){
  int segundos, minutos, horas;
  scanf("%d", &segundos);
  minutos = segundos / 60;
  segundos = segundos % 60;
  horas = minutos / 60;
  minutos = minutos % 60;
  printf("%d:%d:%d\n", horas, minutos, segundos);
  return 0;
}
