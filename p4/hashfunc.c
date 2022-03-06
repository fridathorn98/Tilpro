#include "hashfunc.h"
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

const int HASHVEKSIZE = 1048576;    // 2 upphöjt till 20 ungefär 1 miljon
//const int HASHVEKSIZE = 2097152     // 2 upphöjt till 21
//const int HASHVEKSIZE = 4194304     // 2 upphöjt till 22

uint32_t tilpro_hash(const char * s) {
  uint32_t hash = 0;
  size_t i = 0;
  while (s[i] != '\0') {
    hash += s[i++];
    hash += hash << 10;
    hash ^= hash >> 6;
  }
  hash += hash << 3;
  hash ^= hash >> 11;
  hash += hash << 13;

  hash = hash & ( HASHVEKSIZE - 1 );
  return hash;
}

void put(Nod ** hashtable, char * key, char value[]) {
  uint32_t index = tilpro_hash(key);
  Nod * s=search(hashtable[index],key); //om den redan finns
  if(s!=NULL){ //omskrivning
    strcpy(s->value,value);
  }
  else{ //om tomt eller krock
    insertnod(&hashtable[index],nynod(key,value));}
}

char * get(Nod ** hashtable, char * key) {
  uint32_t index = tilpro_hash(key);
  Nod * s=search(hashtable[index],key);
  return s->value;
}

void init(Nod ** hashtable){
  for(int i=0;i<HASHVEKSIZE;++i){
    if(hashtable[i]!=NULL){
      clearlist(&hashtable[i]);
      hashtable[i]=NULL;
    }
  }
}

void clearlist(Nod ** pp){ //från föreläsning 15
  if((*pp)->next!=NULL){
    Nod * p = *pp;
    clearlist(&(p->next));
    free(*pp);
  }
}
