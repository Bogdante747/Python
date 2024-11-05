class BinaryTree:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def insert(self, value):
        return self._insert(value, self)
    
    def _insert(self, value, parent_node):
        if value < parent_node.value:
            if parent_node.left is None:
                parent_node.left = BinaryTree(value, parent_node)
            else:
                self._insert(value, parent_node.left)
        elif value > parent_node.value:
            if parent_node.right is None:
                parent_node.right = BinaryTree(value, parent_node)
            else:
                self._insert(value, parent_node.right)

    def search(self, value):
        node = self
        while node:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        return node
    
    def delete(self, value):
        return self._delete(value, self)
    
    def _delete(self, value, node):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                original = node
                node = node.right
                while node.left:
                    node = node.left
                node.right = self._delete(node.value, original.right)
                node.left = original.left
                return node