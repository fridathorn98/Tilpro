#include "hashfunc.h"
// ...

extern const int HASHVEKSIZE;
// ...

int main() {
  Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
  init(myhashvek);

  put(myhashvek, "Adam", "123321");
  put(myhashvek, "Adam", "1"); //skriv över
  put(myhashvek, "Berit", "2");
  char * s = get(myhashvek, "Adam");
  printf("Adam -> value = %s \n", s);
  char * s1 = get(myhashvek, "Berit");
  printf("Berit -> value = %s \n", s1);
  char * s2 = get(myhashvek,"Ej");
  // printf("Ej -> value = %s \n",s2); //får segmentation fault eftersom den inte finns

  //Krock testas genom att ändra return  i tilpro_hash

  init(myhashvek); //ta bort allt
  free(myhashvek);

}
