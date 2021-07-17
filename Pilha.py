from No import No


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            self.topo = self.topo.proximo
            self.tamanho -= 1

    def imprimir(self):
        if self.topo == 0:
            print('Pilha Vazia!') 
        else:
            aux = self.topo
            while(aux): 
                print(aux.dado)
                aux = aux.proximo
            print('------------------------------------------------') 
