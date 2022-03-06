import timeit
from timeit import Timer
import random

#####################################################
#
# timeit
# stmt = the statement you want to measure
# number = number of executions you want to run stmt
# timeit tar tid på : hur lång tid det tar att köra "stmt" "number" gånger
# timeit skriver ut tiden det tar
# anropas via: timeit.timeit(stmt,setup,timer, number)

class latobjekt: #klass med låtobjekten
    def __init__(self,song):
        self.trackid=song[0]
        self.latid=song[1]
        self.artist=song[2]
        self.titel=song[3]

    def __lt__(self, other): #jämför om self<other map artistnamn
        if self.artist < other.artist:
            return True
        else:
            return False

class DictHash: #Dictionary från d1
    def __init__(self):
        self._htab={}
    def __contains__(self,key): #anropas via "in"
        try:
            self._htab[key]
            return True
        except KeyError:
            return False
    def store(self,key,data):
        self._htab[key] = data
    def search(self,key):
        if key in self:
            return self._htab[key]

def readfile(filename,N): #läser in filen och lägger in i lista och hashtab
    f = open(filename) #öppna filen
    file_content_list = f.read().splitlines() #skapa sträng av fildatan
    v=[] #lista
    D=DictHash() #dictionary
    for j,line in enumerate(file_content_list): #gå igenom raderna
        song=line.split('<SEP>')
        if len(song)==4: #nödvändigt, men borde inte vara det
            if not song[2] in D: #om artistnamnet inte redan finns
                if len(v)<N: #för att begränsa
                    s=latobjekt(song) #skapa objekt
                    v.append(s) #lägg in objektet sist i listan
                    D.store(s.artist,s.titel) #lägg in i Dictionary
            else: #om artistnamnet redan finns - uppdatera
                if len(v)<N: #för att begränsa
                    while song[2] in D:
                        song[2]=song[2]+'a' #lägg till a tills unik
                    s=latobjekt(song) #skapa objekt
                    v.append(s) #lägg in objektet sist i listan
                    D.store(s.artist,s.titel) #lägg in i Dictionary
    return v, D #returnera listan och hastabellen

def linsok(lista, testartist): #linjärsökning
    i=0;
    while lista[i].artist!=testartist and i<(len(lista)-1):
        i=i+1
    return lista[i]

def binsok(listan, nyckel): #binärsökning från frl
    if len(listan) == 0: #hittades inte
        return False
    else:
        mitten = len(listan)//2
        if listan[mitten].artist == nyckel: #om hittad
            return True
        else:
            if nyckel < listan[mitten].artist: #om mindre - sök till vänster
                return binsok(listan[:mitten], nyckel)
            else: #om större - sök till höger
                return binsok(listan[mitten+1:], nyckel)

def mergesort(data): #taget från frl
    if len(data) > 1:
        mitten = len(data)//2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        mergesort(vensterHalva)
        mergesort(hogerHalva)

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1
    return data

def quicksort(data): #taget från frl
    sista = len(data) - 1
    qsort(data, 0, sista)
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
        data[v], data[h] = data[h], data[v] #byt plats
        if v >= h: #stoppvillkor
            break
    data[v], data[h] = data[h], data[v]
    return v

class Heap: #taget från frl
    # En max-heap
    def __init__(self,N):
        """Skapar en lista där vi använder element 1..maxsize"""
        self.maxsize = 2*N #ändra så att heapen har rum för alla element
        self.tab = (self.maxsize+1)*[None]
        self.size = 0

    def isEmpty(self):
        """Returnerar True om heapen är tom, False annars"""
        return self.size  == 0

    def isFull(self):
        """Returnerar True om heapen är full, False annars"""
        return self.size == self.maxsize

    def insert(self,song):
        """Lägger in nya data med jämförelsevärde 'artist' i heapen"""
        if not self.isFull():
            self.size += 1
            self.tab[self.size] = latobjekt(song)
            i = self.size
            while i > 1 and self.tab[i//2] < self.tab[i]:
                self.tab[i//2], self.tab[i] = self.tab[i], self.tab[i//2]
                i = i//2

    def delMax(self):
        """Hämtar det största (översta) objektet ur heapen"""
        if not self.isEmpty():
            data = self.tab[1]
            self.tab[1] = self.tab[self.size]
            self.size -= 1
            i = 1
            while i <= self.size//2:
                maxi = self.maxindex(i)
                if self.tab[i] < self.tab[maxi]:
                    self.tab[i],self.tab[maxi] = self.tab[maxi], self.tab[i]
                i = maxi
            return data.data
        else:
            return None

    def maxindex(self, i):
        """Returnerar index för det största barnet"""
        if 2*i+1 > self.size:
            return 2*i
        if self.tab[2*i] > self.tab[2*i+1]:
            return 2*i
        else:
            return 2*i+1
def heapsort(lista,N): #taget från frl
    heap = Heap(N)   #an
    vänd klassen heap
    for s in lista:
        heap.insert([s.trackid,s.latid,s.artist,s.titel]) #stoppa in i heapen
    return heap.tab

def main():
    N=100 #antal element att lägga till i listan
    v,D=readfile("unique_tracks.txt",N) #skapa lista och hashtabell

    n = len(v)
    print("Antal element =", n)

    #Söker efter nästsista  elementet med linjärsökning i osorterade listor.
    testartist = v[n-2].artist #nästsista
    stmt = lambda: linsok(v, testartist)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Linjärsökningen i osorterad lista tog", round(linjtid, 4) , "sekunder")

    #Söker med linjärsökning efter 1000 olika element i en osorterad lista och redovisar genomsnittssökningen.
    i=0
    linjtid=[]
    while i<1000:
        i=i+1
        if i in [100,200,300,400,500,600,700,800,900]:
            print(i) #för uppdatering på hur långt koden kommit
        index=random.randint(0,len(v)-1) #slumpa fram ett index
        testartist = v[index].artist #vilken som söks efter
        stmt = lambda: linsok(v, testartist)
        linjtid.append(timeit.timeit(stmt, number = 50)) #ta tid och lagra i vektor
    print("Linjärsökningen i osorterad lista tog", sum(linjtid)/len(linjtid) , "sekunder i medel")

    #Söker efter nästsista elementet med linjärsökning i sorterade listor.
    sv=mergesort(v) #sortera listan
    testartist = sv[n-2].artist #nästsista
    stmt = lambda: linsok(sv, testartist)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Linjärsökningen i sorterad lista tog", round(linjtid, 4) , "sekunder")

    #Sorterar listor med mergesort
    stmt = lambda: mergesort(v)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Sortering med mergesort tog", round(linjtid, 4) , "sekunder")

    #Sorterar listor med quicksort
    stmt = lambda: quicksort(v)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Sortering med quicksort tog", round(linjtid, 4) , "sekunder")

    #Sorterar listor med heapsort
    stmt = lambda: heapsort(v,N)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Sortering med heapsort tog", round(linjtid, 4) , "sekunder")

    #Söker med binärsökning i sorterade listor.
    sv=mergesort(v) #sortera listan
    testartist = sv[random.randint(0,len(v)-1)].artist #random element
    stmt = lambda: binsok(sv, testartist)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Binärsökningen i sorterad lista tog", round(linjtid, 4) , "sekunder")

    #Slår upp element i Pythons inbyggda dictionary
    testartist = v[random.randint(0,len(v)-1)].artist #random element
    stmt = lambda: D.search(testartist)
    linjtid = timeit.timeit(stmt, number = 50)
    print("Sökning i dictionaryn tog", round(linjtid, 4) , "sekunder")

main()

###############################################
# Teoretisk analys
# Stämmer dina resultat med teorin?
#       Ja. Se tabell och matlab fil
# De algoritmer som enligt teorin är linjära, är de det i praktiken?
#       Ja. Se matlab fil
