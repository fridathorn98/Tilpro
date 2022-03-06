#include "lista.h"

Nod * nynod(char name[],int tel){ //skapa en ny nod
  Nod * ny =  malloc(sizeof(Nod));
  (*ny).tel=tel; //lägg in telefonnummer
  int i=0;
  while(name[i]){ //alternativet till strcpy()
    ny->name[i]=name[i]; i++; //lägg in namn
  }
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
  printf("name = %s \n",p->name);
  printf("tel = %d \n",p->tel);
}

void printlist(Nod * p){ //input = 1a noden
  while(p != NULL){
    printnod(p);
    p=p->next;
  }
};

Nod * search(Nod * p, int tel){
  while(p!=NULL){
    if(p->tel == tel){break;} //stoppvillkor
    else{p=p->next;}
  }
  return p;
};
