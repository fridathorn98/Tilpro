#include "lista.h"

Nod * nynod(char * key,char value[]){ //skapa en ny nod
  Nod * ny =  malloc(sizeof(Nod));
  ny->key=key;
  strcpy(ny->value,value);
  ny -> next = NULL;
  ny -> prev = NULL;
  return ny;
};

void insertnod(Nod ** padr, Nod * tobeadded){
  if(*padr==NULL){ //om tom
    *padr = tobeadded; //lägg in som enda noden
  }
  else{
   tobeadded -> next = *padr;
   (*padr) -> prev = tobeadded;
   *padr = tobeadded;
  }
};

void removenod(Nod ** padr, Nod * toberemoved){
  if(toberemoved->next!=NULL && toberemoved->prev!=NULL){ //mitten-nod
    (toberemoved->prev)->next = (toberemoved->next);
    (toberemoved->next)->prev = (toberemoved->prev);
  }
  else if(toberemoved->next!=NULL && toberemoved->prev==NULL){ //första-noden
    Nod * root = toberemoved->next;
    *padr = root; //lägg in som första
  }
  else if(toberemoved->next==NULL && toberemoved->prev!=NULL){ //sista-noden
    (toberemoved->prev)->next = NULL;
  }
  free(toberemoved); //frigör minne
};

void printnod(Nod * p){
  if(p!=NULL){
    printf("key = %s \n",p->key);
    printf("value = %s \n",p->value);
  }
  else{printf("Noden finns inte\n");}
}

void printlist(Nod * p){ //input = 1a noden
  while(p != NULL){
    printnod(p);
    p=p->next;
  }
};

Nod * search(Nod * p, char * key){
  while(p!=NULL){
    if(strcmp(p->key,key)==0){break;} //stoppvillkor
    else{p=p->next;}
  }
  return p;
};

// Testning - kommentera bort
// int main() {
//   Nod * root = NULL;
//
//   // Skapa listan C-3, B-2, A-1
//     Nod* A=nynod("A",1);    insertnod(&root,A);
//     Nod* B=nynod("B",2);    insertnod(&root,B);
//     Nod* C=nynod("C",3);    insertnod(&root,C);
//
//   printf("Grundlistan:\n");
//   printlist(root);
//   removenod(&root,B);
//   printf("Nod B borttagen:\n");
//   printlist(root);
//   Nod * S = search(root,1);
//   printf("Sökt nod 1 : \n");
//   printnod(S);
//   Nod * S = search(root,2);
//   printf("Sökt nod 2 : \n");
//   printnod(S);
//   Nod * S = search(root,3);
//   printf("Sökt nod 3 : \n");
//   printnod(S);
//
//   //Töm listan
//   removenod(&root,C);
//   removenod(&root,A);
//   //removenod(&root,root);
//
// }
