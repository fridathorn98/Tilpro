import timeit
from timeit import Timer
import random

class latobjekt: #klass med låtobjekten
    def __init__(self,song):
        # artistid	artistnamn	sångtitel	låtlängd	år
        self.artistid=song[0]
        self.artistnamn=song[1]
        self.titel=song[2]
        self.length=song[3]
        self.year=song[3]

    def __lt__(self, other): #jämför om self<other map låtlängd
        if float(self.length) < float(other.length):
            return True
        else:
            return False

def readfile(filename): #läser in filen och lägger in i lista
    f = open(filename) #öppna filen
    file_content_list = f.read().splitlines() #skapa sträng av fildatan
    v=[] #lista
    for j,line in enumerate(file_content_list): #gå igenom raderna
        song=line.split('\t')
        if len(song)==5: #nödvändigt, men borde inte vara det
            s=latobjekt(song) #skapa objekt
            v.append(s) #lägg in objektet sist i listan
    return v #returnera listan

def metod_1(lista, k): #linjärsökning k ggr
    for kk in range(0,k): #linjärsök genom listan och ta bort den längsta
        longest=lista[0] #återställ
        for i in range(0,len(lista)): #sök igenom alla element och hitta största
            if lista[i]>longest: #om större
                longest=lista[i]
        if kk<(k-1): # om ej sista iterationen
            lista.remove(longest) #ta bort den längsta
        elif kk==(k-1): #om sista iterationen
            return longest

def quicksort(data): #taget från frl
    sista = len(data) - 1
    qsort(data, 0, sista)
    return data
def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)
def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v

def metod_2(lista,k):
    v_sort=quicksort(lista)
    return v_sort[len(v_sort)-k] #då den hamnar i fel ordning

def main():
    # EGEN TESTNING
    v=readfile("sang-artist-data.txt") #skapa lista
    n = len(v)
    print("Antal element =", n)
    k=3
    print(metod_1(v,k).titel)
    v=readfile("sang-artist-data.txt") #gör om pga användning av remove
    print(metod_2(v,k).titel)

    k = 1
    song_list=readfile("sang-artist-data.txt")

    while k <= 30:
       time_1 = timeit.timeit(stmt = lambda: metod_1(song_list, k), number = 1)
       time_2 = timeit.timeit(stmt = lambda: metod_2(song_list, k), number = 1)

       print(k, time_1, time_2)

       k += 4

main()

####################################################
# Teoretisk analys
# Kommer de båda metoderna alltid att ge samma svar, för samma k?
#     Ja, det borde de göra
# Vad har de båda metoderna för respektive komplexitet?
#     metod_1 har O(k) och metod_2 har O(1)
#       linjärsökning vs sortering av lista (konstant) och åtkomst av element i tabell
# För de 999 988 stycken låtarna i sang_artist_data.txt,
#   uppskatta teoretiskt för vilket k den ena metoden är snabbare än den
#   andra och vice versa. Vid vilket k är de lika snabba?
#       metod_1 tar N*k operationer och metod_2 tar för insättningen
#       N*log(N) och O(1) för åtkomst. Därmed kommer metod_2 bli snabbare
#       vid ca k=log(N)
