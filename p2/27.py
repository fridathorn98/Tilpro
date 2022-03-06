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

def get_file_content(file_name): #hämta många lösenord
    #print("IN = ",file_name)
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("Fel")
        sys.exit()

    file_content = infil.readlines()
    #print("OUT = ",file_content)
    return file_content

def save_file_content(file_name, list_of_combinations): #spara lösenorden (kopierat från uppgiften)
    with open(file_name, 'w') as f:
        for item in list_of_combinations:
            f.write("%s\n" % item)

def main(): #gör alla kombinationer
    out=[] #för ett ord
    output=[] #för alla ord (alla kombinationer)
    all_passwords=get_file_content('p2_passwords.txt') #hämta alla olika lösenord
    #print(all_passwords)
    for password in all_passwords:
        word=str(password[:-1]) #ta bort /n
        out=[word] #lägg in i out vektorn
        out=out+storbokstav(word) #kombinationer i en stor bokstav
        out=out+tvåstora(word) #kombinationer i två stora bokstäver
        outh=out #hjälpvariabel till nästa loop
        for i, x in enumerate(outh): #fixar specialtecken
            #print(x)
            out=out+skjutinspecial(x)

        output=output+out #lägg till kombinationerna av ordet till resten

    save_file_content('p2_comb.txt',output)

main()
