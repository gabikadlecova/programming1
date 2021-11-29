class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.root is None:
            self.root = node
            return

        curr = self.root
        while True:
            # we need to save this so that we know where to add the node
            next_left = curr.val > node.val

            # this is the same as:
            # if next_left:
            #    next = curr.left
            # else:
            #    next = curr.right
            next_node = curr.left if next_left else curr.right

            if next_node is None:
                if next_left:
                    curr.left = node
                else:
                    curr.right = node
                return

            curr = next_node

    def print_postorder(self):
        pass

    def print_inorder(self):
        pass

    def print_preorder(self):
        pass