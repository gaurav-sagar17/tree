# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def helper(node) :
            if(not node) :
                return -1

            if(not node.left and not node.right):
                self.arr.append(1)
                return 1

            l = helper(node.left ) 
            r = helper(node.right ) 

            if(l  == r  and l>0) :
                # if(self.arr[-1] == self.arr[-2] ) :

                self.arr.append((2*self.arr[-1])+1)
                return (2*self.arr[-1])+1
            
            return -2

        helper(root) 
        self.arr.sort(reverse=True) 
        if(len(self.arr) < k):
            return -1 

        return self.arr[k-1] 

        
