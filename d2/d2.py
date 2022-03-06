
# ###########################################################
#
# Klass DictHash med pythons inbyggda dictionary


class DictHash:
    def __init__(self):
        self.hash=None

    def store(self,key,data):
        if self.hash==None: #om tom
            self.hash = {key: data}
        else:
            self.hash[key] = data

    def search(self,key):
        return self.hash[key]


############################################################
#
# Spara in unique_tracks.txt till DictHash
# filhantering delvis tagen från p1

def read_data(file_name): #läser in txt datan
    f = open(file_name) #öppna filen
    file_content_list = f.read() #skapa sträng av fildatan
    f.close() #stäng
    file_content_list=file_content_list.splitlines() #dela upp i rader
    return file_content_list #returnera lista med alla rader i filen

file_content_list=read_data("unique_tracks.txt")
d=DictHash()
for j,line in enumerate(file_content_list): #gå igenom raderna
    line=line.split('<SEP>') #dela upp raden i ord
    for i,x in enumerate(line): #gå igenom orden för att hitta key och data
        if i==2: #key
            key=x #artist
        elif i==3: #data
            data=x #låt
    d.store(key,data) #lägg in i hashtabellen
print(j)

print(d.search('Karkkiautomaatti')) #exempel på något som ligger i listan

############################################################
#
# Egen implementation av hashtabellen med krockhantering
#

class HashNode:
    def __init__(self):
        self.key=None
        self.value=None

class Hashtabell:
    def __init__(self):
        self.size=101 #"lagom"
        self.table=[None]*self.size

    def hashfunktion(self,key): #få fram hash_key
        fold=0 #använd folding metoden
        for a in str(key):
            fold+=ord(str(a)) #gör om key till int och addera
        return fold %self.size #ta modulu för att passa in i hash-tabellen

    def store(self,key,data): #data läggs in i tabellen mha key
        hash_key=self.hashfunktion(key) #ta fram hash_key
        node=HashNode() #skapa ny nod
        if self.table[hash_key]==None or key==self.table[hash_key].key:
        #om tom eller upprepad (skrivs över)
            node.key=key
            node.value=data
            self.table[hash_key]=node #lägg in data i tabellen på rätt ställe
        else: #kollision
            while self.table[hash_key]!=None: #linear probing without clustering
                hash_key+=3
                hash_key=hash_key % self.size #för att inte gå förbi size
                if hash_key==self.hashfunktion(key): #om vi gått ett varv
                    print("No free spot") #om listan är full
                    break
            if self.table[hash_key]==None: #om vi hittat ledig plats på uppdaterad hash_key
                node.key=key
                node.value=data
                self.table[hash_key]=node

    def search(self,key):
        hash_key=self.hashfunktion(key) #ta fram hash_key
        if self.table[hash_key]==None: #om tom
            return 'KeyError: '+"'"+key+"'"
        elif self.table[hash_key].key==key: #om ej kollision
            return self.table[hash_key].value
        else: #om kollision
            while self.table[hash_key].key!=key: #linear probing igen
                hash_key+=3
                hash_key=hash_key % self.size
                if hash_key==self.hashfunktion(key): #om ej hittad på ett varv
                    return 'KeyError: '+"'"+key+"'"
                    break
            if self.table[hash_key].key==key: #om hittad
                return self.table[hash_key].value

############################################################
#
# Egen testning
# AB och BA kommer krocka
# AB ska skrivas om från 1 till 3

d=Hashtabell()
d.store('AB','1')
d.store('BA','2')
d.store('AB','3')
#print(d.search('BA'))
#print(d.search('AB'))


############################################################
#
# Testning av Hashtabell
#$ curl http://www.csc.kth.se/~lk/unique_tracks.txt > unique_tracks.txt
#

d=Hashtabell()
file_content_list=read_data('unique_tracks.txt')
for j,line in enumerate(file_content_list): #gå igenom raderna
    line=line.split('<SEP>') #dela upp raden i ord
    if j<100: #tar för lång tid att köra igenom alla
        for i,x in enumerate(line): #gå igenom orden för att hitta key och data
            if i==2: #key
                key=x
            elif i==3: #data
                data=x
        d.store(key,data) #lägg in i hashtabellen

print(d.search('Karkkiautomaatti'))


############################################################
#
# Redovisning
# Insättning och sökning genomförs genom att hash indexet beräknas och
# sedan läggs noden in där mha en pekare.
# Man söker i hashtabellen genom att beräkna indexet och sedan kolla om den
# ligger där. Annars genomförs iteration för krockhantering
# Hashtabeller ger snabb sökning eftersom man vet var det man söker efter ligger
# det som kostar mest är hashfunktionen
