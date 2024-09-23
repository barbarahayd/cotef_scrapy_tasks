# Implementação de uma árvore n-ária em Python

# Classe Node: contém o valor do nó e uma lista de filhos e um método para adicionar um nó filho à lista de filhos. A lista de filhos é inicializada como vazia. 

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []
    # método para adicionar um nó filho à lista de filhos
    def adicionar_filho(self, no_filho):
        self.filhos.append(no_filho)


# Classe Tree: contém a raiz da árvore e métodos para adicionar nós e percorrer a árvore.

class Tree:
    def __init__(self, raiz):
        self.raiz = raiz
    # método para adicionar um nó filho à árvore
    def adicionar_no(self, pai, filho):
        pai.adicionar_filho(filho)
    # método para percorrer a árvore em preorder
    def percorrer_preorder(self, no_atual):
        """Retorna os valores dos nós em uma travessia preorder (raiz, filhos)"""
        valores = [no_atual.valor]
        for filho in no_atual.filhos:
            valores.extend(self.percorrer_preorder(filho))
        return valores
