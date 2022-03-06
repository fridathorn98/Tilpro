#include "lista.h"

int main() {
  Nod * root = NULL;

  // Skapa listan C-3, B-2, A-1
    Nod* A=nynod("A",1);    insertnod(&root,A);
    Nod* B=nynod("B",2);    insertnod(&root,B);
    Nod* C=nynod("C",3);    insertnod(&root,C);

  printf("Grundlistan:\n");
  printlist(root);
  removenod(&root,C);
  printf("Nod C borttagen:\n");
  printlist(root);
  Nod * S = search(root,3);
  printf("Sökt nod : \n");
  printnod(S);

  //Töm listan
  removenod(&root,C);
  removenod(&root,A);
  //removenod(&root,root);

}
