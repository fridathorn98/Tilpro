#include <stdio.h>

int main() {
  printf("Hej välkommen till 21-spelet\n");
  printf("Vi börjar från 0 och ökar i tur och ordning med antingen 1 eller 2, den som först kommer till 21 vinner!!!\n");
  printf("Exempel:\n du säger   1\n jag säger  2\n du säger   4\n jag säger  6\n du säger   8\n jag säger 10\n du säger  12\n jag säger 14\n du säger  18\n jag säger 20\n du säger 21 och vinner!!!\n\n");
  for (int summa = 3; summa <= 21; summa += 3) {
    printf("Vilket tal säger du? ");
    int tal = 0;
    while ( 1 ) {
      scanf("%d", &tal);
      //om bokstäver istället för tal matas in så fastnar programmet i else
      if (summa - tal == 1 || summa - tal == 2)
    break;
      else {
        printf("%d",tal);
    printf("Hallå där, du kan bara öka med 1 eller 2\n");
    printf("Vi var på %d, Vilket tal säger du? ", summa - 3);
    // raden ovan printar texten. %d är en placeholder och håller platsen
    // det som står efter kommmatecknet, dvs summa-3
      }
    }
    printf("Jag säger %d\n", summa);
  }
  printf("Jag vann !!!\n");
}

// Programmet vinner alltid eftersom den hela tiden mellan stegen adderar med tre
// Det spelar ingen roll vad jag skriver in eftersom den oavsett gör 3,6,9,12,15,18,21
