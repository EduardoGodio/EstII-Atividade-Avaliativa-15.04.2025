# Integrantes: Eduardo Godio Rodrigues, Talles Martins Pereira, Felipe Angelo Zucolotto Moura e Luis Henrique Gomes Zortea
# Turma: CC5N
#
# Atividade 1 [0,3 pontos]: Em acordo com cada um dos diagramas a seguir, implemente suas travessias, indicando os resultados
# e o tipo específico de travessia proposto.
# a) Imagem indica uma travessia in_order | b) Imagem indica uma travessia pre_order | c) Imagem indica uma travessia pos_order

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child  = None

def post_order(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node.data)

        if node.left_child:
            stack1.append(node.left_child)
        if node.right_child:
            stack1.append(node.right_child)

    return stack2[::-1]

def in_order(root):
    result = []
    stack = []
    current = root

    while current is not None or stack:
        while current:
            stack.append(current)
            current = current.left_child

        current = stack.pop()
        result.append(current.data)

        current = current.right_child

    return result

def pre_order(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right_child:
            stack.append(node.right_child)
        if node.left_child:
            stack.append(node.left_child)

    return result

# Montagem da árvore do exercício
root = Node("1")
n2 = Node("2")
n3 = Node("3")
root.left_child = n2
root.right_child = n3

n4 = Node("4")
n2.left_child = n4

n5 = Node("5")
n6 = Node("6")
n3.left_child = n5
n3.right_child = n6

n7 = Node("7")
n8 = Node("8")
n5.left_child = n7
n5.right_child = n8

# Saída
print("a) In-Order")
print(in_order(root))

print("b) Pre-Order")
print(pre_order(root))

print("c) Post-Order")
print(post_order(root))