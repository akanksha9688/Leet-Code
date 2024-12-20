# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: if the tree is empty, return the root (None)
        if not root:
            return root
        
        # Queue for level order traversal
        queue = deque([root])
        
        # Boolean flag to keep track of whether we are at an odd level
        is_odd_level = False
        
        # Perform level order traversal
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level_nodes = []
            
            # Process nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # Add the current node to the list for this level
                current_level_nodes.append(node)
            
            # If we are at an odd level, reverse the node values
            if is_odd_level:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    # Swap the values of the nodes at the two ends
                    current_level_nodes[left].val, current_level_nodes[right].val = \
                        current_level_nodes[right].val, current_level_nodes[left].val
                    left += 1
                    right -= 1
            
            # Toggle the flag to switch to the next level (odd to even, or even to odd)
            is_odd_level = not is_odd_level
        
        # Return the root after modifying the tree
        return root