class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def set_value(self, value):
        self.value = value
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def get_value(self):
        return self.value
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert_element(self, value):
        if not self.root:
            self.root = Node( value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node( value)

                        break
                    else :
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = Node( value)

                        break
                    else :
                        current = current.right
                else:
                    break


            
    def delete_element(self, value):#<----
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.min_value_node(node.right)
                node.value = temp.value
                node.right = self._delete_recursive(node.right, temp.value)
        return node
    
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def display_pre_order(self,node):
        if node :
            print(node.value,end=" ")
            self.display_pre_order(node.left)
            self.display_pre_order(node.right)
    def display_in_order(self,node):
        if node:
            self.display_in_order(node.left)
            print(node.value,end=" ")
            self.display_in_order(node.right)
    def display_post_order(self,node):
        if node:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.value,end=" ")
    def total_elements(self,node):
        if node is None:
            return 0    
        if node:
            l=self.total_elements(node.left)
            r=self.total_elements(node.right)
            return 1+l+r
    
bst = BinarySearchTree()
bst.insert_element(50)
bst.insert_element(30)
bst.insert_element(20)
bst.insert_element(40)
bst.insert_element(70)
bst.insert_element(60)
bst.insert_element(80)
root=bst.root

print("Pre-order Traversal:", end=" ")
bst.display_pre_order(root)
print("\nIn-order Traversal:", end=" ")
bst.display_in_order(root)
print("\nPost-order Traversal:", end=" ")
bst.display_post_order(root)
print("\nTotal Elements:", bst.total_elements(root))

bst.delete_element(20)
bst.delete_element(30)
bst.delete_element(50)

print("\nAfter deletion:")
print("Pre-order Traversal:", end=" ")
bst.display_pre_order(root)
print("\nIn-order Traversal:", end=" ")
bst.display_in_order(root)
print("\nPost-order Traversal:", end=" ")
bst.display_post_order(root)
print("\nTotal Elements:", bst.total_elements(root))

