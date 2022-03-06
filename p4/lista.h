#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifndef LISTA_H
#define LISTA_H

//#include "lista.h"	/* leta lokalt  */
//#include <system_lista.h>	/* leta i systemet */

struct nod {
    char * key;
    char value[512];
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

Nod * nynod(char * key,char value[]);
void insertnod(Nod ** padr, Nod * tobeadded);
void removenod(Nod ** padr, Nod * toberemoved);
void printnod(Nod * p);
void printlist(Nod * p);
Nod * search(Nod * p, char * key);

#endif
