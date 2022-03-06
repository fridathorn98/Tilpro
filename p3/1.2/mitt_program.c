#include <stdio.h> //för att få tillgång till scanf, fscanf, printf
//om man tar bort den så går det inte att kompilera
#include <time.h>

int getyear() {
    time_t timer;
    time(&timer);
    struct tm* tm_info = localtime(&timer);
    return tm_info->tm_year + 1900;
}

//const int maxlength = 30;
extern const int maxlength;  //importera

int main() {
    printf("Hej vad heter du? ");
    char str [maxlength];
    scanf("%s", str); //det funkar oavsett längd på namnet

    int age;
    printf("Hur gammal är du? ");
    fscanf(stdin, "%d", &age);

    int thisyear = getyear();

    printf("Hej %s, i år är det %d. ", str, thisyear);
    if (2000 + age == thisyear)
	printf("Du skulle kunna vara född på 1900-talet\n");
    else if (2000 + age > thisyear)
	printf("Du är född på 1900-talet!\n");
    else
	printf("Du är född på 2000-talet!\n");
}
