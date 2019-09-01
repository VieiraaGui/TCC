class Nos:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value= value
        self.left = left
        self.right = right

class Tree:

    def __init__(self):
        self.root = Nos(None, None, None, None)
        self.root = None

    def inserir(self, v):
       novo = Nos(v, None, None)
       if self.root == None:
          self.root = novo
       else:
            atual = self.root
         while True:
             anterior = atual
            if v <= atual.item:
                atual = atual.left
                if atual == None:
                  anterior.esq = novo
                     return

            else: 
                atual = atual.right
                if atual == None:
                     anterior.right = novo
                     return

        
