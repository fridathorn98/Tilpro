#include <stdlib.h>
#include <stdio.h>
#include <string.h>

long foo(void * a) {
    long offset = 4196518;
    long adr = (long) a;
    return adr - offset;
}

int main(int argc, char * argv[]) {
    int a = 1;
    char tkn = 't';
    int v[] = {1, 3, 5};

    int * vdyn = malloc(sizeof(int) * 2);
    vdyn[0] = 7;
    vdyn[1] = 4;

    char * staticstr = "Hej";

    char * sv = malloc(sizeof(char) * 11);
    strcpy(sv, staticstr);    // kopierar sträng se frl-anteckningar

    printf("variabel        adress            värde\n");
    printf("---------------------------------------\n");
    printf("a               %p      %d\n"      , &a        , a);
    printf("tkn             %p      %c\n"      , &tkn      , tkn);
    printf("v               %p      %d \n"     , v         , *v);
    printf("v[1]            %p      %d \n"     , (v + 1)     , *(v + 1));
    printf("v[2]            %p      %d \n"     , (v + 2)     , *(v + 2));
    printf("vdyn            %p      %d \n"     , vdyn       , *vdyn);
    printf("vdyn[1]         %p      %d \n"     , (vdyn + 1)   , *(vdyn + 1));
    printf("staticstr       %p         %c \n"     , staticstr   , *staticstr);
    printf("staticstr[1]       %p      %c \n"     , staticstr+1   , *(staticstr+1));
    printf("staticstr[2]       %p      %c \n"     , staticstr+1   , *(staticstr+2));
    printf("sv              %p      %c \n"     , sv   , *sv);
    printf("sv[1]          %p       %c \n"     , sv+1   , *(sv+1));
    printf("sv[2]          %p       %c \n"     , sv+2   , *(sv+2));
    printf("foo             %p      \n"        , &foo);
    printf("---------------------------------------\n");
    printf("variabel       adress (long)       värde\n");
    printf("---------------------------------------\n");
    printf("a               %ld      %d\n"      ,(long)  &a        , a);
    printf("tkn             %ld      %c\n"      ,(long)  &tkn      , tkn);
    printf("v               %ld      %d \n"     ,(long)  v         , *v);
    printf("v[1]            %ld      %d \n"     ,(long)  (v + 1)    , *(v + 1));
    printf("v[2]            %ld      %d \n"     ,(long)  (v + 2)     , *(v + 2));
    printf("vdyn            %ld      %d \n"     ,(long)  vdyn       , *vdyn);
    printf("vdyn[1]         %ld      %d \n"     ,(long)  (vdyn + 1)   , *(vdyn + 1));
    printf("staticstr       %ld           %c \n"     ,(long)  staticstr   , *staticstr);
    printf("staticstr[1]    %ld           %c \n"     , (long)(staticstr+1)   , *(staticstr+1));
    printf("staticstr[2]    %ld           %c \n"     , (long)(staticstr+2)   , *(staticstr+2));
    printf("sv              %ld      %c \n"     ,(long)  sv   , *sv);
    printf("sv[1]           %ld      %c \n"     , (long)(sv+1)   , *(sv+1));
    printf("sv[2]           %ld      %c \n"     , (long)(sv+2)   , *(sv+2));
    printf("foo             %ld      \n"        ,(long)  &foo);
}

// Variablerna hamnar inte på samma ställe
// när programmet körs (och kompileras) flera gånger.
