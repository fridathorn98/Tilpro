
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
