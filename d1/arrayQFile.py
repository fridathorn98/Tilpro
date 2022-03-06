from array import array

class ArrayQ:

    def __init__(self):
        self.A=array('l',[])

    def enqueue(self,input): #utöka listan med 'input' längst bak
        self.A.append(input)

    def dequeue(self): #tar bort det som står först
        if not self.isEmpty(): #om inte tom
            return self.A.pop(0)

    def isEmpty(self): #kolla om listan är tom
        if len(self.A)==0:
            return True
        else:
            return False
