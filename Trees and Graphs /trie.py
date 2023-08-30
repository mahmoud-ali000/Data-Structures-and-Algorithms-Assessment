# https://www.geeksforgeeks.org/trie-insert-and-search/


class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        
        self.isEndOfWord = False

class Trie():
    
    def __init__(self) -> None:
        self.root = TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        current = self.root
        for level in range(len(key)):
            # chr exists
            if current.children[self._charToIndex(key[level])]:
                current = current.children[self._charToIndex(key[level])]
            else:
                current.children[self._charToIndex(key[level])] = TrieNode()
                current = current.children[self._charToIndex(key[level])]
            
        current.isEndOfWord = True

    def search(self, key):
        current = self.root
        for level in range(len(key)):
            if current.children[self._charToIndex(key[level])]:
                current = current.children[self._charToIndex(key[level])]
            else:
                return False
        return current.isEndOfWord

if __name__ == '__main__':
    test_trie = Trie()
    test_trie.insert('aa')
    print(test_trie.root.children)
    print(test_trie.root.children[0].children)
    print(test_trie.root.children[0].children[0].isEndOfWord)
    print(test_trie.search('a'))
    print(test_trie.search('aa'))
    test_trie.insert('a')
    print(test_trie.search('a'))
                
                    
