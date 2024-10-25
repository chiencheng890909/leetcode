class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.dirs = []

    def insert(self, dir):
        cur = self.root

        for i in range(len(dir)):
            if dir[i] not in cur.children.keys():
                cur.children[dir[i]] = TrieNode()
            elif cur.children[dir[i]].is_word:
                return
            cur = cur.children[dir[i]]
        cur.is_word = True

    def SearchAll(self, cur, sen):
        if cur.is_word:
            self.dirs.append(sen)
            return
        for key, value in cur.children.items():
            self.SearchAll(cur.children[key], sen + ("/" + key))


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        root = Trie()
        for path in folder:
            root.insert(path.split("/")[1:])
        root.SearchAll(root.root, "")
        return root.dirs
        
