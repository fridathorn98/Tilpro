from array import array

############################################################
#
# Experiment med array
#

x=array('l', [1,2,3,4,5]) #skapa array med datatypen integer

x.append(6) #lägger till en 6a sist
#print(x)
x.insert(1,0) #lägger till 0 på plats 1 och flyttar resten
#print(x)
x.remove(0) #tar bort elementet med värdet 0
#print(x)
x.pop(0) #tar bort den på plats 0
#print(x)



# Jag vill använda append till enqueue
# Jag vill använda pop(0) till dequeue

############################################################
#
# Klassen ArrayQ
# (ligger numera i filen arrayQFile som importeras här)

from arrayQFile import ArrayQ

############################################################
#
# Testa klassen ArrayQ
#   inklistrat från uppgiften

def basictest():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("test OK")
    else:
        print("FAILED expexted x=1 and y=2 but got x =", x, " y =", y)

basictest()

############################################################
#
# Trollkarlsprogrammet med ArrayQ
# Inget returneras i programmet, utan korten printas i den ordningen de läggs ut

def troll(kort):
    queue=ArrayQ()
    for x in kort: #lägg in korten i kön
        queue.enqueue(x)
    while not queue.isEmpty():
        x=queue.dequeue() #plocka ut första värdet
        queue.enqueue(x) #lägg in det första värdet sist
        output=queue.dequeue() #ta bort det nya första värdet
        print(output)

kortlek=[7,1,12,2,8,3,11,4,9,5,13,6,10] #gör så outputen är ordnad rätt

#troll(kortlek)

############################################################
#
# LinkedQ - test
#

from linkedQFile import LinkedQ #importera

Q=LinkedQ()
#print('Kön är tom = ',Q.isEmpty()) #kollar om kön är tom
Q.enqueue(1) #lägg till ett element
Q.dequeue() #ta bort elementet
#print('Kön är tom efter att ha tagit bort och lagt till element = ',Q.isEmpty())
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
#print('Kön är tom när tre element lagts till =',Q.isEmpty())
x1=Q.dequeue()
x2=Q.dequeue()
x3=Q.dequeue()
#print('De tre elementen som plockas ur är: ',x1,x2,x3)

############################################################
#
# Trollkarlsprogrammet med LinkedQ
# allt är samma utom att jag använder LinkedQ

def troll(kort):
    queue=LinkedQ() #använd LinkedQ istället!
    for x in kort: #lägg in korten i ArrayQ
        queue.enqueue(x)
    while not queue.isEmpty():
        x=queue.dequeue() #plocka ut första värdet
        queue.enqueue(x) #lägg in det första värdet sist
        output=queue.dequeue() #ta bort det nya första värdet
        print(output)

#kortlek=[3,1,5,2,4]
kortlek=[7,1,12,2,8,3,11,4,9,5,13,6,10]

troll(kortlek)

############################################################
#
# Redovisning
#

# För pythons array metoder se överst "Experiment med array"
# Attributen ska vara privata för att man inte ska kunna ändra dem utanför klassen
# Båda implementationerna fungerar. Skillnaden är hur de byggs upp
# antingen byggs de upp med python listor eller noder och pekare (länkade listor)

############################################################
#
# Testa remove()
#   om en vill se vad Q=LinkedQ() innehåller så används Q.visa()

# Skapa en länkad lista med 3 noder och ta bort mitten
Q=LinkedQ()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.remove(2)
# Försök ta bort ett element som inte finns i en kö med några noder
Q.remove(5) #blir oförändrad
# Ta bort sista elementet i en kö med några noder
Q.enqueue(4)
Q.remove(4)
# Ta bort första elementet i en kö med en nod
Q=LinkedQ()
Q.enqueue(1)
Q.remove(1)
#Försök ta bort ett  element ur en tom kö
Q=LinkedQ()
Q.remove(1) #inget ska hända och programmet ska inte krascha
