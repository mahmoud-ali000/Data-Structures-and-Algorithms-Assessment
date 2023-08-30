from binary_tree import display_keys

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
    def disp(self, nesting=0):
        indent = " " * nesting*2
        output = f'{self.value}\n'
        if self.left is not None:
            output += f'{indent}L:'
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f'{indent}L:'
            output += self.right.disp(nesting + 1)
        return output

def minimal_tree(arr:list) -> Node:
    mid = len(arr) // 2
    if mid != 0:
        left = arr[:mid]
        right = arr[mid+1:]
    
    # for left like [0]
    elif arr:
        return Node(arr[0])
    
    # for right like None
    else:
        return None
    
    root = Node(arr[mid])
    root.left = minimal_tree(left)
    root.right = minimal_tree(right)
    return root
    
if __name__ == '__main__':
    test_arr = list(range(4))
    print(test_arr)
    test_arr = minimal_tree(test_arr)
    display_keys(test_arr)
    print(f'root value={test_arr.key}')

    display_keys(minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]))
