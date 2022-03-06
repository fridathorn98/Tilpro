#include <stdlib.h>
#include <stdio.h>

#ifndef LISTA_H
#define LISTA_H

//#include "lista.h"	/* leta lokalt  */
//#include <system_lista.h>	/* leta i systemet */

struct nod {
    char name[30];
    int tel;
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

Nod * nynod(char name[],int tel);
void insertnod(Nod ** padr, Nod * tobeadded);
void removenod(Nod ** padr, Nod * toberemoved);
void printnod(Nod * p);
void printlist(Nod * p);
Nod * search(Nod * p, int tel);

#endif
