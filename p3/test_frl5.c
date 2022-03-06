
#include <stdio.h>
#include <stdlib.h>

int main() {
  int size = 3;
  int *vek= malloc(sizeof(int) * size);

  for (int i=0; i<size; i++){
  printf("vek[%d] = %d, at %p \n",i,*(vek+i),vek+i);

  }


}
