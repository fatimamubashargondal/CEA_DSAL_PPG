class BookNode: #basic variables
    def __init__ (self , isbn, title, author, year, category,copies):
        self.isbn = isbn
        self.book_data = {
            'title': title, 'author': author, 'year': year,
            'category': category, 'available_copies': int(copies)
        }
        self.left = None
        self.right = None
        self.height = 1
        
class BookCatalog: #avl tree
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0 
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        #checking the node's position
        x = y.left
        T2 = x.right
        #implementing the rotation
        x.right = y
        y.left = T2
        #rebalancing 
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x #new root

    def rotate_left(self, x):
        #checking the node's position
        y = x.right
        T2 = y.left
        #implementing the rotation
        y.left = x
        x.right = T2
        #rebalancing 
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y #new root
    
    def rebalance(self, node):
        # Update height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        # Left Heavy
        if balance > 1:
            if self.get_balance(node.left) < 0: # Left-Right Case
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right Heavy
        if balance < -1:
            if self.get_balance(node.right) > 0: # Right-Left Case
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    def insert(self, root, isbn, title, author, year, category,copies ):
        if not root:
            return BookNode(isbn, title, author, year, category,copies)
        if isbn <root.isbn:
            root.left = self.insert(root.left, isbn, title, author, year, category,copies)
        elif isbn> root.isbn:
            root.right = self.insert(root.right, isbn,title, author, year, category,copies)
        else:
            return root 
        #rebalance
        return self._rebalance(root)
    
    def delete(self, root, isbn):
        if not root:
            return root
    
        if isbn < root.isbn:
            root.left = self.delete(root.left, isbn)
        elif isbn > root.isbn:
            root.right = self.delete(root.right, isbn)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
    
            # Node with two children: get inorder successor
            temp = self.search_min(root.right)
            root.isbn = temp.isbn
            root.book_data = temp.book_data
            root.right = self.delete(root.right, temp.isbn)
        #rebalance   
        return self._rebalance(root)
        
    def search(self,root,isbn):
        if root is None:
            return None
        if isbn == root.isbn:
            return root
        elif isbn< root.isbn:
            return self.search(root.left, isbn)
        else:
            return self.search(root.right, isbn)
        
    def search_min(self, root):
        if root is None:
            return None
        current = root
        while current.left:
            current = current.left
        return current 

    def inorder_traversal(self, root):
        result = []
        stack = []
        current = root
    
        while current or stack:
            # Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left
    
            current = stack.pop()
            result.append(current.isbn)
    
            current = current.right
    
        return result

