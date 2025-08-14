from collections import deque


class Treenode:
    def __init__(self, val=0,left=None, right=None ) :
        self.val = val
        self.left = left
        self.right=right
        
class Solution():
     def levelOrder(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)

        return result


root = Treenode(10)
root.left = Treenode(12)
root.right = Treenode(23)
root.left.left = Treenode(32)
root.right.right = Treenode(33)

obj = Solution()
print(obj.levelOrder(root))
