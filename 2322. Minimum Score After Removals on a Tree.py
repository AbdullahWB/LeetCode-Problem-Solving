"""
2322. Minimum Score After Removals on a Tree
https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/description/
"""


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        INF = float("inf")  # Use float('inf') for infinity, more Pythonic
        N = len(nums)

        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # is_ancestor[u][v] = True if u is an ancestor of v in the DFS tree rooted at 0
        is_ancestor = [[False] * N for _ in range(N)]

        # This DFS builds the is_ancestor matrix
        # It marks all nodes in the current path from root to 'node' as ancestors of 'node'
        def dfs(node, parent, ancestors):
            # For every ancestor in the current path, mark it as an ancestor of the current node
            for a in ancestors:
                is_ancestor[a][node] = True

            # Recursively call DFS for children
            for v in adj_list[node]:
                if v != parent:
                    # Add current node to the list of ancestors for its children
                    ancestors.append(node)  # Corrected: used .append instead of ,append
                    dfs(v, node, ancestors)
                    # Backtrack: remove current node from ancestors list when returning from child
                    ancestors.pop()

        # Start the first DFS from node 0 with no initial ancestors
        dfs(0, -1, [])

        # xs will store the XOR sum of the subtree rooted at each node
        xs = [0] * N  # Initialize with 0s

        # This DFS calculates the XOR sum of each subtree
        def dfs2(node, parent):
            current_xor_sum = nums[node]  # Start with the node's own value
            for v in adj_list[node]:
                if v != parent:
                    # XOR sum with children's subtree XOR sums
                    current_xor_sum ^= dfs2(v, node)
            xs[node] = current_xor_sum  # Store the subtree XOR sum for the current node
            return current_xor_sum

        # Start the second DFS from node 0 to populate xs array
        dfs2(0, -1)  # No xsum parameter needed here, it's calculated recursively

        total_xor_sum = xs[
            0
        ]  # The XOR sum of the entire tree is xs[0] (subtree of root)
        best = INF  # Initialize best difference to infinity

        # Iterate through all possible pairs of edges to remove
        # An edge (u, v) removal effectively splits the tree into two components.
        # Removing two edges splits it into three components.
        # We consider removing edges (parent_a, a) and (parent_b, b)
        # The nodes 'a' and 'b' represent the roots of the subtrees formed by cutting the edges above them.
        for a in range(1, N):  # 'a' can be any node except the root (0)
            for b in range(a + 1, N):  # 'b' can be any node after 'a'
                xa = xs[a]  # XOR sum of subtree rooted at 'a'
                xb = xs[b]  # XOR sum of subtree rooted at 'b'

                components = []
                if is_ancestor[a][b]:
                    # Case 1: 'a' is an ancestor of 'b'
                    # Cutting edge above 'a' and edge above 'b'
                    # Component 1: subtree of 'b' (xb)
                    # Component 2: subtree of 'a' excluding subtree of 'b' (xa ^ xb)
                    # Component 3: rest of the tree (total_xor_sum ^ xa)
                    components = [xb, xa ^ xb, total_xor_sum ^ xa]
                elif is_ancestor[b][a]:
                    # Case 2: 'b' is an ancestor of 'a'
                    # Symmetric to Case 1
                    components = [xa, xb ^ xa, total_xor_sum ^ xb]
                else:
                    # Case 3: 'a' and 'b' are in different branches (neither is ancestor of the other)
                    # Component 1: subtree of 'a' (xa)
                    # Component 2: subtree of 'b' (xb)
                    # Component 3: rest of the tree (total_xor_sum ^ xa ^ xb)
                    components = [xa, xb, total_xor_sum ^ xa ^ xb]

                # Sort the component XOR sums to easily find min and max
                components.sort()
                # Calculate the difference between the maximum and minimum XOR sums
                delta = components[-1] - components[0]
                # Update the best (minimum) difference found so far
                best = min(best, delta)

        return best
