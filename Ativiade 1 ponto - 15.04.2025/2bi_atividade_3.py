# Integrantes: Eduardo Godio Rodrigues, Talles Martins Pereira, Felipe Angelo Zucolotto Moura e Luis Henrique Gomes Zortea
# Turma: CC5N
#
# Atividade 3 [0,1 pontos]: Construa uma árvore binária cujas saídas das travessias são as seguintes:
# Inorder: 4 2 1 7 5 8 3 6
# Postorder: 4 2 7 8 5 6 3 1 

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
print("In-Order")
print(in_order(root))

print("Post-Order")
print(post_order(root))