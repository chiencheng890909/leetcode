class Node:
    def __init__(self):
        self.val = {}
        self.IsEndOfWord = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        temp = self.root
        for char in word:
            if char not in temp.val:
                temp.val[char] = Node()
            temp = temp.val[char]
        temp.IsEndOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for char in word:
            if char not in temp.val:
                return False
            temp = temp.val[char]

        return temp.IsEndOfWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for char in prefix:
            if char not in temp.val:
                return False
            temp = temp.val[char]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
