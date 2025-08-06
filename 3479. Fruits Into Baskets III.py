"""

Segment Tree implementation for the problem of placing fruits into baskets.
This code defines a Segment Tree that allows efficient querying and updating of basket capacities.
3479. Fruits Into Baskets III
https://leetcode.com/problems/fruits-into-baskets-iii

"""


class SegmentTree:
    def __init__(self, arr: List[int]):
        # Sentinel value to mark a basket as used. Since capacities are positive (>=1), 0 works.
        self.USED_BASKET_CAPACITY = 0
        self.N = len(arr)
        self.arr = list(arr)  # Make a mutable copy of the original basket capacities
        # The tree array will store the maximum capacity in each segment.
        # A size of 4*N is a common safe upper bound for segment tree arrays.
        self.tree = [0] * (4 * self.N)
        # Build the segment tree starting from the root (node 1, covering full range [0, N-1])
        self.build(1, 0, self.N - 1)

    def build(self, node: int, start: int, end: int):
        """
        Recursively builds the segment tree. Each node stores the maximum capacity
        in its corresponding range of basket indices.
        """
        # Base case: If it's a leaf node (representing a single basket)
        if start == end:
            self.tree[node] = self.arr[start]  # Store the actual capacity of the basket
            return

        mid = (start + end) // 2
        left_child_idx = 2 * node
        right_child_idx = 2 * node + 1

        # Recursively build the left child for range [start, mid]
        self.build(left_child_idx, start, mid)
        # Recursively build the right child for range [mid + 1, end]
        self.build(right_child_idx, mid + 1, end)

        # The current node (parent) stores the maximum capacity found in its children's ranges
        self.tree[node] = max(self.tree[left_child_idx], self.tree[right_child_idx])

    def update(self, node: int, start: int, end: int, idx: int, value: int):
        """
        Updates the capacity of a basket at 'idx' to 'value' (typically 0 to mark as used).
        Propagates changes up the tree to maintain maximums.
        """
        # Base case: If we've reached the leaf node corresponding to the target index
        if start == end:
            self.arr[idx] = value  # Update the actual basket capacity in the array
            self.tree[node] = value  # Update the segment tree node's value
            return

        mid = (start + end) // 2
        left_child_idx = 2 * node
        right_child_idx = 2 * node + 1

        # Decide which child's range contains the 'idx' and recurse
        if start <= idx <= mid:
            self.update(left_child_idx, start, mid, idx, value)
        else:
            self.update(right_child_idx, mid + 1, end, idx, value)

        # After updating a child, recalculate the current node's maximum capacity
        # based on the (potentially updated) values of its children.
        self.tree[node] = max(self.tree[left_child_idx], self.tree[right_child_idx])

    def _query(self, node: int, start: int, end: int, fruit_quantity: int) -> int:
        """
        Recursively queries the segment tree to find the leftmost index
        with a basket capacity greater than or equal to 'fruit_quantity'.
        Returns the index if found, -1 otherwise.
        """
        # Pruning condition: If the maximum capacity in the current range is
        # less than the required 'fruit_quantity', then no basket in this
        # entire range can hold the fruit.
        if self.tree[node] < fruit_quantity:
            return -1

        # Base case: If it's a leaf node (representing a single basket)
        # We've already passed the `self.tree[node] < fruit_quantity` check,
        # so this basket must be suitable. Return its index.
        if start == end:
            return start

        mid = (start + end) // 2
        left_child_idx = 2 * node
        right_child_idx = 2 * node + 1

        # Strategy for "leftmost":
        # First, try to query the left child's range.
        # Check if the left child's range (represented by its max capacity)
        # contains any basket with sufficient capacity.
        if self.tree[left_child_idx] >= fruit_quantity:
            result = self._query(left_child_idx, start, mid, fruit_quantity)
            if (
                result != -1
            ):  # If a suitable basket was found in the left half, return its index.
                return result

        # If no suitable basket was found in the left child's range (or its max was too small),
        # then search in the right child's range.
        if self.tree[right_child_idx] >= fruit_quantity:
            return self._query(right_child_idx, mid + 1, end, fruit_quantity)

        # If neither child yields a suitable basket (this should ideally not be reached
        # if the initial `self.tree[node] < fruit_quantity` check was passed,
        # but it's a safe fallback).
        return -1

    def query(self, fruit_quantity: int) -> int:
        """Public method to start the query from the root of the tree."""
        return self._query(1, 0, self.N - 1, fruit_quantity)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        # Handle edge case for empty inputs
        if n == 0:
            return 0

        # Initialize the Segment Tree with the basket capacities.
        # This takes O(N) time.
        st = SegmentTree(baskets)

        unplaced_fruits_count = 0

        # Iterate through each fruit type from left to right as per the problem rules.
        # This loop runs N times.
        for fruit_quantity in fruits:
            # Query the segment tree for the leftmost available basket that can hold this fruit.
            # This query operation takes O(log N) time.
            index = st.query(fruit_quantity)

            if index == -1:
                # If no suitable basket is found, increment the count of unplaced fruits.
                unplaced_fruits_count += 1
            else:
                # If a suitable basket is found, mark it as used in the segment tree.
                # This is done by updating its capacity to 0 (or a sentinel value).
                # The update operation takes O(log N) time.
                st.update(1, 0, n - 1, index, st.USED_BASKET_CAPACITY)

        # Return the total count of fruit types that could not be placed.
        return unplaced_fruits_count
