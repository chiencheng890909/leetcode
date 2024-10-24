# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def check_tree(cur1, cur2):
            if not cur1 and not cur2:
                return True
            
            if not cur1 or not cur2 or cur1.val != cur2.val:
                return False

            return (check_tree(cur1.left, cur2.left) or check_tree(cur1.left, cur2.right)) and (check_tree(cur1.right, cur2.left) or check_tree(cur1.right, cur2.right))

        return check_tree(root1, root2)
            


        
