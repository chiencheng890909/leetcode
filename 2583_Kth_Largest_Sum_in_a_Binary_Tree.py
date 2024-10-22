# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        Ans = []

        def BFS(cur, layer):
            if len(Ans) < layer + 1:
                Ans.append([cur.val])
            else:
                Ans[layer].append(cur.val)
            if cur.left is not None:
                BFS(cur.left, layer + 1)
            
            if cur.right is not None:
                BFS(cur.right, layer + 1)
            
        
        BFS(root, 0)

        if k > len(Ans):
            return -1
            
        for i in range(len(Ans)):
            Ans[i] = sum(Ans[i])
        Ans.sort(reverse=True)
        return Ans[k - 1]

        
        
