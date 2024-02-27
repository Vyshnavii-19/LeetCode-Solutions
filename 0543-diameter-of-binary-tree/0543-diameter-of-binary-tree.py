class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:   
        def find_longest_path(root):
            if not root:
                return -1
            left = find_longest_path(root.left)+1
            right = find_longest_path(root.right)+1
            self.longest_path = max(self.longest_path, left + right)
            return max(left, right)
            
        self.longest_path = 0
        find_longest_path(root)
        return self.longest_path