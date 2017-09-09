# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #runtime：28ms
        if not t1 and not t2:
            return
        if not t1:
            ans=t2
        elif not t2:
            ans=t1
        else:
            ans=TreeNode(t1.val+t2.val)
            ans.left=self.mergeTrees(t1.left,t2.left)
            ans.right=self.mergeTrees(t1.right,t2.right)
        return ans


#另一种方法   #runtime：35ms         
        
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:return None
        ans=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
        ans.left=self.mergeTrees(t1 and t1.left,t2 and t2.left)
        ans.right =self.mergeTrees(t1 and t1.right ,t2 and t2.right)
        return ans
'''这里面有两个难点一个是if...else...三元表达式，另外一个就是t1 and t1.left理解了

t1.val if t1 else 0写成普通形式就是
if t1:
    return t1.val
else:
    return

t1 and t1.left理解，首先要知道and的含义
and从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值。
t1和t1.left都存在的话，返回的是t1.left
t1存在，t1.left不存在，返回的还是t1.left
t1不存在，t1.left存在，返回的是t1（本题不存在这种情况，没有t1就没有t1.left）
t1不存在，t1.left不存在，返回的还是t1（本题不存在这种情况，没有t1就没有t1.left）
所以总结起来：如果and左值为真，返回的是and右值；如果and左值为假，返回的是and左值'''


        
        
    
