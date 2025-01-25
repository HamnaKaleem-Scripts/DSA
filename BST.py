class Node:
    def __init__(self, query, urls=None, filename=None):
        self.query = query
        self.urls = urls
        self.filename = filename
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_value(self, query, urls=None, filename=None):
        self.root = self.insert(self.root, query, urls, filename)

    def insert(self, root, query, urls=None, filename=None):
        if not root:
            return Node(query, urls, filename)
        elif query < root.query:
            root.left = self.insert(root.left, query, urls, filename)
        else:
            root.right = self.insert(root.right, query, urls, filename)
        return root

    def search(self, root, query):
        if root is None or root.query == query:
            return root
        if query < root.query:
            return self.search(root.left, query)
        return self.search(root.right, query)

    def search_value(self, query):
        return self.search(self.root, query)