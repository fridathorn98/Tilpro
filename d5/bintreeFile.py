class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

class Bintree:
    def __init__(self):
        self.root = None

    def store(self, key, newvalue):
        # Sorterar in newvalue i trädet
        self.root = rekstore(self.root, key, newvalue)

    def search(self, key):
        # returnerar value om key finns i trädet, KeyError annars
        return reksearch(self.root,key)

    def __contains__(self, key):
        try:
            self.search(key)
            if self.search(key)==None:
                return False
            else:
                return True
        except: #försök alltid skriva
            return False

    def write(self):
        # Skriver ut trädet i inorder
        rekwrite(self.root)

# Följande funktioner ligger utanför klassen
# Vet ej varför då det fungerar om de ligger inuti också (se test.py)

def rekstore(root, key, newvalue):
    if root==None: #om trädet är tomt
        return Node(key,newvalue)
    else: #skapa ny nod
        if root.key==key: #uppdatera värdet
            root.value=newvalue
        elif key > root.key and root.right!=None: #skapa ny
            rekstore(root.right,key,newvalue) #leta vidare
        elif key > root.key and root.right==None: #skapa ny
            nynod=Node(key,newvalue) #skapa ny nod
            root.right=nynod #lägg till pekare
        elif key < root.key and root.left!=None: #leta vidare
            rekstore(root.left,key,newvalue) #leta vidare
        elif key < root.key and root.left==None: #leta vidare
            nynod=Node(key,newvalue) #skapa ny nod
            root.left=nynod #lägg till pekare
        return root

def reksearch(root,key):
    if root!=None: #hitta en tom plats
        if root.key==key: #hittad
            return root.value
        elif key > root.key and root.right!=None:
            return reksearch(root.right,key)
        elif key < root.key and root.left!=None:
            return reksearch(root.left,key)
        else:
            raise KeyError
    else: #om ej hittad
        raise KeyError

def rekwrite(root): #inorder
    if root != None:
        rekwrite(root.left)
        print(root.value)
        rekwrite(root.right)

# EGEN TESTNING
# svenska = Bintree()               # Skapa ett trädobjekt
# svenska.store("gurka", "grönsak") # Sortera in "gurka" i trädet
# svenska.store("gurka", "gulsak") # Uppdatera value
# svenska.store("alpha", "anna")
# svenska.store("beta", "beta")
# svenska.store("l", "L")
# svenska.store("m", "m")
# svenska.store("h", "h")
# svenska.store("p", "p")
# svenska.store("aa", "stol")
#
# if "gurka" in svenska:            # Kolla om "gurka" finns i trädet
#     print("Ordet finns i svenska ")# Operatorn in anropar metoden __contains__
#
# a=svenska.search("alpha")
# print('alpha har värdet: ',a) #test av search
# print('INORDER:')
# svenska.write()            # Skriver alla trädobjektets ord i bokstavsordning
