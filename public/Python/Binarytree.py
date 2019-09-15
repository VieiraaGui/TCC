





class No:
     
     def __init__(self, key, amd, intel):
          self.item = key
          self.amd = amd
          self.intel = intel
          self.ger7 = ger7
          self.ger8 = ger8

class Tree:

     def __init__(self):
          self.root = No(None,None,None)
          self.root = None

     def inserir(self, socket):
          novo = No(socket,None,None) 
          if self.root == None:
               self.root = novo
          else: 
               atual = self.root
               while True:
                    anterior = atual
                    
                    if socket = "am4":
                         atual = atual.amd
                         if atual == None:
                                anterior.amd = novo
                                return
                    
                    else:
                         atual = atual.intel
                         if atual == None:
                                 anterior.intel = novo  
                                    if gen <= 7:
                                        anterior.ger7 = novo
                                        else:
                                            anterior.ger8 = novo
                                 return
                

     def buscar(self, chave):
         if self.root == None:
              return None 
         atual = self.root 
         while atual.item != chave: 
               if chave < atual.item:
                    atual = atual.amd 
               else:
                    atual = atual.intel 
               if atual == None:
                    return None 
             return atual
