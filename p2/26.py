def stor(bokstav): #uppgift 2.1
  alfabeta = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z':'Z'}
  if bokstav in alfabeta: #om liten
    storbokstav=alfabeta[bokstav]
  else: #om den redan är stor
    storbokstav=bokstav
  return storbokstav

def storbokstav(ord): #uppgift 2.2
    vek=list(ord) #gör om string till vektor så itereration är möjlig
    komb=[] #tom vektor för att lagra alla kombinationer
    for i, x in enumerate(vek): #iterera över bokstäverna
        if stor(x)!=x: #om bokstaven inte redan är stor
            vek[i]=stor(str(x)) #ändrar bokstaven på plats i till stor
            komb.append("".join(vek)) #lägg till det ändrade ordet som string i vektorn
            vek=list(ord) #nollställ till grundordet
    return komb

def tvåstora(ord): #uppgift 2.3
    vek=list(ord) #gör om string till vektor så itereration är möjlig
    komb=[] #tom vektor för att lagra alla kombinationer
    for i in range(0,len(vek)):
        for j in range(i+1,len(vek)):
            vek[i]=stor(str(vek[i])) #ändrar första bokstaven till stor
            vek[j]=stor(str(vek[j])) #ändrar andra bokstaven till stor
            komb.append("".join(vek)) #lägg till det ändrade ordet som string i vektorn
            vek=list(ord) #nollställ till grundordet
    return komb

def skjutinspecial(ord): #uppgift 2.4
    specialtecken=['2','3','+']
    vek=list(ord) #gör om string till vektor så itereration är möjlig
    komb=[]
    for i in range(0,len(vek)+1): #index för var specialtecknet ska ligga
        for x in specialtecken: #vilket specialteckensom skjuts in
            vek.insert(i,x) #lägg in specialtecknet
            komb.append("".join(vek)) #gör om till string och lägg in i v
            vek=list(ord) #återställ
    return (komb)

def main(): #uppgift 2.5
    input="fyra"

    out=[input] #spara grundordet i outputen
    out=out+storbokstav(input)
    out=out+tvåstora(input)

    #print(out) #test

    outh=out #hjälpvariabel för ej evig loop

    for i, x in enumerate(outh): #skjutinspecial för varje kombination
        out=out+skjutinspecial(x)

    print(out)

main()

#Uppgift 2.6
#----------------------------------------------
#Skriv ner antal ordkombinationer (längden på listan) du får för olika långa ord.
# (4 st specialtecken)
# 1->14 , 2->40 , 3->91 , 4->176 , 5->304 ,
# 6->484 , 7->725 , 8->1036 , 9->1426 , 10->1904
# Resultatet ger en kurva som är ungefär y=28.25x^2-109.15x+132.7
#, där x är antal tecken och y är antal ordkombinationer som fås
# Dvs, y=O(x^2)

#Variera antal siffror/specialtecken som skjuts in i ett givet ord och räkna antal ordkombinationer
# (givet ord = "fyra")
# 1->66 , 2->121 , 3->176 , 4->231 , 5->286 ,
# 6->341 , 7->396 , 8->451 , 9->506 , 10->561
# Resultatet ger en kurva som är ungefär y=55x+11
#, där x är antal specialtecken och y är antal ordkombinationer som fås
# Dvs, y=O(x)
