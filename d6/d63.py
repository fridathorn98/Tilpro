import sys

if len(sys.argv) < 3:
   print("parametrar saknas")
   sys.exit()
else:
   print("parameter 1 är",  sys.argv[1], " och parameter 2 är", sys.argv[2])



class Node:
    def __init__(self):
        self.value=None
        self.next=None

class LinkedQ:
    def __init__(self):
        self.__first=None #privata attribut mha __
        self.__last=None

    def enqueue(self,input): #lägg till ny nod
        nod=Node() #skapa en ny nod
        nod.value=input #ansätt värde
        if self.isEmpty(): #om tom
            self.__first=nod
            self.__last=nod
        else:
            self.__last.next=nod #skapa pil mellan sista noden och den nya
            self.__last=nod #ansätt den nya till den sista

    def dequeue(self): #ta bort första noden. Value ges som output
        if self.isEmpty(): #om tom
            return None
        if self.__first==self.__last:
            out=self.__first.value
            self.__first=None
            self.__last=None
            return out
        else:
            out=self.__first.value
            self.__first=self.__first.next
            return out

    def isEmpty(self): #kolla om tom
        if self.__first==None:
            return True
        else:
            return False

    def remove(self,input): #ta bort nod med value=input
        if not self.isEmpty(): #om ej tom
            if self.__first.value==input: #om den första ska tas bort
                self.__first=self.__first.next #första = nod 2
            else:
                nod=self.__first #startvärde för iteration
                while nod.next.next!=None:
                    if nod.next.value==input: #om vi vill ta bort nästa nod
                        nod.next=nod.next.next #peka om så att nästa blir nästnästa
                    else: #om vi ej vill ta bort den
                        nod=nod.next #iterera till nästa nod
                if self.__last.value==input: #om vi vill ta bort sista noden
                    self.__last=nod #peka om sista till näst sista
                    nod.next=None

def makechildren(ord,barn):
    giltiga=word3()
    barn.store(ord,ord) #lägg in ordet
    alfabeta = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    komb=[]
    for i, x in enumerate(ord):
        for a in alfabeta:
            word=list(ord) #gör ordet till vektor & nollställer
            if x!=a: #lägg inte in samma ord
                word[i]=a #ändra bokstav
                word1="".join(word) #lägg ihop till string
                if giltiga.search(word1)!=None and not word1 in barn:#.__contains__(word1): #om giltigt och ej finns
                    komb.append(word1) #lägg in i kombinationer-outputen
                    barn.store(word1,word1) #lägg in i DictHash
    return komb, barn #returna barnen som pythonlista (=komb) och hashlista (=barn)

class DictHash: #från d1
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

def word3(): #hämtar alla giltiga ord
    word3 = open('word3.txt','r').readlines() #hämta innehållet från word3.txt
    giltiga=DictHash()
    for line in word3:
        line=line.split('\n')
        giltiga.store(line[0],line[0]) #lägg in i hashtabellen
    return giltiga

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def writechain(ParentNode): #skriver ut vägen
    if ParentNode==None: # om tom från början
        print('Det finns ingen väg')
    elif ParentNode.parent!=None: #om den har föräldrar - iterera ett steg upp
        Parent = ParentNode.parent
        return (writechain(Parent) +'->'+ ParentNode.word)
    else: #om stamfader -> skriv ut ordet
        return ParentNode.word

def sok(startord,slutord): #söker om det finns en väg eller inte
    queueOfWords=LinkedQ()
    barn=DictHash()
    P=ParentNode(startord)
    queueOfWords.enqueue(P)
    while not queueOfWords.isEmpty():
        nextWord = queueOfWords.dequeue()
        if nextWord.word == slutord: #om hittad
            break;
        else:
            komb,barn=makechildren(nextWord.word,barn)
            for ord in komb:
                tmp=ParentNode(ord,nextWord)
                queueOfWords.enqueue(tmp)
    if queueOfWords.isEmpty(): #om ej hittad
        return None
    else:             #om hittad
        return nextWord

import sys

if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()
else:
    P=sok(sys.argv[1],sys.argv[2])
    print('Kortaste vägen är ',writechain(P))
