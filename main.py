"""
Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função para inserir elementos, uma para
imprimir os elementos na ordem que foram inseridos e uma função para imprimir os elementos na ordem inversa a que foram
inseridos.
"""

from Pilha import Pilha

pilha = Pilha()

pilha.imprimir()

pilha.adicionar("Computador")
pilha.imprimir()
pilha.adicionar("Notebook")
pilha.imprimir()

pilha.empilhar("Tablet")
pilha.empilhar("Smartphone")

pilha.imprimir()


print("----- Removendo ------")

pilha.remover()
pilha.remover()
pilha.empilhar("Relógio")

pilha.imprimir()

pilha.remover()
pilha.remover()
pilha.remover()