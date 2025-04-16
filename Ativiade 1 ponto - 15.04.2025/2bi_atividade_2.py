# Integrantes: Eduardo Godio Rodrigues, Talles Martins Pereira, Felipe Angelo Zucolotto Moura e Luis Henrique Gomes Zortea
# Turma: CC5N
#
# Atividade 1 [0,4 pontos]: A partir dos códigos estudados em sala, escreva um algoritmo eficiente para verificar se duas árvores binárias
# são idênticas ou não. Observe que duas árvores binárias serão idênticas se tiverem estrutura idêntica e seus conteúdos também o forem.
#
# Input:        1               1
#             /   \           /   \
#            2     3         2     3
#           / \   / \       / \   / \
#          4   5 6   7     4   5 6   7
# Output: True
# Explanation: Ambas as árvores têm a mesma estrutura e o mesmo conteúdo.
#
# Input:        1               1
#             /   \           /   \
#            2     3         2     3
#           / \   / \       / \   / 
#          4   5 6   7     4   5 6   
# Output: False
# Explanation: As árvores têm estrutura diferentes.
#
# Input:        1               1
#             /   \           /   \
#            2     3         2     3
#           / \   / \       / \   / \
#          4   5 6   7     4   5 6   8
# Output: False
# Explanation: As árvores têm a mesma estrutura, porém com valores de nós diferentes.

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child  = None

def identity(root1, root2):
    stack = [(root1, root2)]

    while stack:
        n1, n2 = stack.pop()

        # Se ambos são None, continua (subárvore vazia)
        if not n1 and not n2:
            continue
        else:
            if n1 is None:
                print(f"# <-> {n2.data}")
            elif n2 is None:
                print(f"{n1.data} <-> #")
            else:
                print(f"{n1.data} <-> {n2.data}")

        # Se um é None e o outro não, estrutura diferente
        if not n1 or not n2:
            print("Explanation: As árvores têm estrutura diferentes.")
            return False

        # Se os dados são diferentes
        if n1.data != n2.data:
            print("Explanation: As árvores têm a mesma estrutura, porém com valores de nós diferentes.")
            return False

        # Empilha os filhos da direita e da esquerda
        stack.append((n1.left_child, n2.left_child))
        stack.append((n1.right_child, n2.right_child))

    print("Explanation: Ambas as árvores têm a mesma estrutura e o mesmo conteúdo.")
    return True

# Criação da primeira árvore
root1 = Node("1")
n2 = Node("2")
n3 = Node("3")
root1.left_child = n2
root1.right_child = n3

n4 = Node("4")
n5 = Node("5")
n2.left_child = n4
n2.right_child = n5

n6 = Node("6")
n7 = Node("7")
n3.left_child = n6
n3.right_child = n7

# Criação da segunda árvore
root2 = Node("1")
n2_2 = Node("2")
n3_2 = Node("3")
root2.left_child = n2_2
root2.right_child = n3_2

n4_2 = Node("4")
n5_2 = Node("5")
n2_2.left_child = n4_2
n2_2.right_child = n5_2

n6_2 = Node("6")
n7_2 = Node("7")
n3_2.left_child = n6_2
n3_2.right_child = n7_2

# Criação da terceira árvore
root3 = Node("1")
n2_3 = Node("2")
n3_3 = Node("3")
root3.left_child = n2_3
root3.right_child = n3_3

n4_3 = Node("4")
n5_3 = Node("5")
n2_3.left_child = n4_3
n2_3.right_child = n5_3

n6_3 = Node("6")
n3_3.left_child = n6_3

# Criação da quarta árvore
root4 = Node("1")
n2_4 = Node("2")
n3_4 = Node("3")
root4.left_child = n2_4
root4.right_child = n3_4

n4_4 = Node("4")
n5_4 = Node("5")
n2_4.left_child = n4_4
n2_4.right_child = n5_4

n6_4 = Node("6")
n8_4 = Node("8")
n3_4.left_child = n6_4
n3_4.right_child = n8_4

# Saída
print("Primeiro Caso: Idênticas")
identity(root1, root2)
print("\nSegundo caso: Estrutura diferente")
identity(root1, root3)
print("\nTerceiro caso: Valores diferentes")
identity(root1, root4)