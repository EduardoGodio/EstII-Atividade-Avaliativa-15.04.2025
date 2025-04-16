# Integrantes: Eduardo Godio Rodrigues, Talles Martins Pereira, Felipe Angelo Zucolotto Moura e Luis Henrique Gomes Zortea
# Turma: CC5N
#
# Atividade 4 [0,2 pontos]: A partir dos códigos estudados, considerando a árvore binária a seguir, escreva um algoritmo iterativo para imprimir
# o caminho da fola á raiz para cada nó folha, O uso de recursão é proibido.
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#      / \
#     8   9

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child  = None

def path_to_root(root):
    if root is None:
        return

    # Stack de tuplas: (nó atual, caminho até aqui)
    stack = [(root, [])]

    while stack:
        current, path = stack.pop()

        # Novo caminho incluindo o nó atual
        new_path = path + [current.data]

        # Se for nó folha, imprime o caminho (invertido: folha → raiz)
        if current.left_child is None and current.right_child is None:
            print(" -> ".join(map(str, reversed(new_path))))
        else:
            if current.right_child:
                stack.append((current.right_child, new_path))
            if current.left_child:
                stack.append((current.left_child, new_path))


# Criando a árvore
root = Node("1")
n2 = Node("2")
n3 = Node("3")
root.left_child = n2
root.right_child = n3

n4 = Node("4")
n5 = Node("5")
n2.left_child = n4
n2.right_child = n5

n6 = Node("6")
n7 = Node("7")
n3.left_child = n6
n3.right_child = n7

n8 = Node("8")
n9 = Node("9")
n6.left_child = n8
n6.right_child = n9

# Imprime os caminhos das folhas até a raiz
path_to_root(root)