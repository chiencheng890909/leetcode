# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def BFS_SUM(cur, depth, temp):
            if cur == None:
                return 

            if depth + 1 > len(temp):
                temp.append(0)

            if cur.left != None and cur.right != None:
                cur.left.val = cur.left.val + cur.right.val
                cur.right.val = cur.left.val
            
            if cur.left != None:
                temp[depth] += cur.left.val
            elif cur.right != None:
                temp[depth] += cur.right.val

            BFS_SUM(cur.left, depth + 1, temp)
            BFS_SUM(cur.right, depth + 1, temp)

        def BFS_SWITCH(cur, depth, temp):
            if cur == None:
                return 

            if cur.val == temp[depth - 1]:
                cur.val = 0
            elif cur.val < temp[depth - 1]:
                cur.val = temp[depth - 1] - cur.val

            BFS_SWITCH(cur.left, depth + 1, temp)
            BFS_SWITCH(cur.right, depth + 1, temp)
        
        temp = [root.val]
        BFS_SUM(root, 1, temp)

        BFS_SWITCH(root, 1, temp)
        return root
        
