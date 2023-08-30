import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1
    
    # https://www.programiz.com/python-programming/property
    @property
    def left_size(self):
        if self.left:
            return self.left.size
        return 0
    
    @property
    def right_size(self):
        if self.right:
            return self.right.size
        return 0


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key) -> Node:
        current = self.root
        while current:
            if key <= current.key:
                current.size += 1
                if current.left is None:
                    current.left = Node(key)
                    return current.left
                current = current.left
            
            else:
                current.size += 1
                if current.right is None:
                    current.right = Node(key)
                    return current.right
                current = current.right
        raise f'something went wrong...'
    
    def find(self, key) -> Node:
        '''BFS'''
        queue = [self.Node]
        while queue:
            current = queue.pop(0)
            if current != None:
                if current.key == key:
                    return current
            queue.append(current.left)
            queue.append(current.right)
        return -1
    
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-4.php
    def delete(self, root, key) -> Node:
        # if root doesn't exist, just return it
        if not root:
            return root

        if root.val > key:
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        
        # root.value == key
        else:
            if not root.right:
                self.size -= 1
                return root.left
            elif not root.left:
                self.size -= 1
                return root.right
            
            # if both left and right children exist in the node replace its value w/
            # the minimum value in the right subtree. Now delete theat minimun node in the right subtree
            temp = root.right
            mini_val = temp.val
            while temp.left:
                temp = temp.left
                mini_val = temp.val
            
            root.right = self.delete(root.right, mini_val)
            self.size -= 1
        return root

    def getRandomNode(self):
        random.choices(
            [self.root, self.left, self.right]
        )        


if __name__ == '__main__':
    bst = BST(Node(10))
    bst.insert(5)

    print(bst.insert(5).key)
    print(bst.root.left.key)
