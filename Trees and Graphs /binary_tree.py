# https://jovian.ai/aakashns/python-binary-search-trees


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def parse_tuple(data: tuple):
    if isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node

def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + '∅')
        return

    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


class Traverse:
    def in_order(node):
        if node is None:
            return []
        return Traverse.in_order(node.left) + [node.key] + Traverse.in_order(node.right)
    
    def pre_order(node):
        if node is None:
            return []
        return [node.key] + Traverse.pre_order(node.left) + Traverse.pre_order(node.right)
    
    def post_order(node):
        if node is None:
            return []
        return Traverse.post_order(node.left) + Traverse.post_order(node.right) + [node.key]
            

if __name__ == '__main__':
    test_tree = parse_tuple((
        (1, 3, None), 2, ( (None, 3, 4), 5, (6, 7, 8) )
    ))
    
    # display_keys(None)
    display_keys(test_tree)
    print(Traverse.in_order(test_tree))
    print(Traverse.pre_order(test_tree))
    print(Traverse.post_order(test_tree))
    
