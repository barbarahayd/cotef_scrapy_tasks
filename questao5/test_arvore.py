import unittest
from arvore import Node, Tree

class TestArvore(unittest.TestCase):
    # método setUp é executado antes de cada teste
    def setUp(self):
        # estrutura básica para testes
        self.raiz = Node('Raiz')
        self.arvore = Tree(self.raiz)
        self.filho1 = Node('Filho 1')
        self.filho2 = Node('Filho 2')
        self.arvore.adicionar_no(self.raiz, self.filho1)
        self.arvore.adicionar_no(self.raiz, self.filho2)
    
    # verifica se o nó é adicionado corretamente à árvore
    def test_adicionar_no(self):
        """Testa se um nó é adicionado corretamente."""
        filho_novo = Node('Filho Novo')
        self.arvore.adicionar_no(self.raiz, filho_novo)
        self.assertIn(filho_novo, self.raiz.filhos)

    # verifica se a travessia preorder da árvore está correta
    def test_percorrer_preorder(self):
        """Testa a travessia preorder da árvore."""
        esperado = ['Raiz', 'Filho 1', 'Filho 2']
        resultado = self.arvore.percorrer_preorder(self.raiz)
        self.assertEqual(resultado, esperado)
# executa os testes
if __name__ == '__main__':
    unittest.main()