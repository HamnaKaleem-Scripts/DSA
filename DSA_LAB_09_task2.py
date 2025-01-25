class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def display_in_order(self):
        self._display_in_order(self.root)
        print()

    def _display_in_order(self, node):
        if node:
            self._display_in_order(node.left)
            print(node.value, end=' ')
            self._display_in_order(node.right)

    def display_post_order(self):
        self._display_post_order(self.root)
        print()

    def _display_post_order(self, node):
        if node:
            self._display_post_order(node.left)
            self._display_post_order(node.right)
            print(node.value, end=' ')

    def construct_from_traversals(self, in_order, pre_order):
        if not in_order or not pre_order:
            return None
        
      
        root_value = pre_order[0]
        root = Node(root_value)
        
      
        root_index = in_order.index(root_value)
     
        left_in_order = in_order[:root_index]
        
        right_in_order = in_order[root_index + 1:]
        
        left_pre_order = pre_order[1:1 + len(left_in_order)]
        right_pre_order = pre_order[1 + len(left_in_order):]
        
        root.left = self.construct_from_traversals(left_in_order, left_pre_order)
        root.right = self.construct_from_traversals(right_in_order, right_pre_order)
        
        return root


# Example 1
bst = BinarySearchTree()
in_order = ['D', 'B', 'E', 'A', 'F', 'C']
pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
bst.root = bst.construct_from_traversals(in_order, pre_order)

print("In-order traversal of constructed BST:")
bst.display_in_order()
print("Post-order traversal of constructed BST:")
bst.display_post_order()

# Example 2
bst2 = BinarySearchTree()
in_order2 = [5, 10, 15, 25, 27, 30, 35, 40, 45, 50, 52, 55, 60, 65, 70, 75, 80, 85, 90, 100]
pre_order2 = [50, 25, 10, 5, 15, 40, 30, 27, 35, 45, 75, 60, 55, 52, 65, 70, 90, 80, 85, 100]
bst2.root = bst2.construct_from_traversals(in_order2, pre_order2)

print("In-order traversal of constructed BST:")
bst2.display_in_order()
print("Post-order traversal of constructed BST:")
bst2.display_post_order()
