class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        temp = []
        for c in expression:
            if c == ')':
                while stack[-1] != '(':
                    temp.append(stack[-1])
                    stack.pop()
                stack.pop()
                if stack[-1] == '|':
                    temp = [max(temp)]
                elif stack[-1] == '&':
                    temp = [min(temp)]
                elif stack[-1] == '!':
                    if temp[0] == 'f':
                        temp[0] = 't'
                    else:
                        temp[0] = 'f'
                
                stack.pop()
                stack.append(temp[0])
                temp = []

            elif c != ',':
                stack.append(c)

        if stack[0] == 'f':
            return False
        return True


                
        
