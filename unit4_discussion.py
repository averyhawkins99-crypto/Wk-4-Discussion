class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree by setting the root to None.
        self.root = None

    def insert(self, value):
        # Insert a value into the BST using a recursive helper method.
        # Insertion depends on whether a value is smaller or larger than the current node:
        # - If smaller, it belongs in the left subtree.
        # - If larger, it belongs in the right subtree.
        # This relationship maintains the BST property at every level of the tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Create a new node when a vacant position (None) is found.
        if node is None:
            return Node(value)

        # Insert smaller values into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Insert larger values into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the updated node reference to relink the tree structure.
        return node

    def search(self, value):
        # Search for a value in the BST using the recursive helper.
        # Returns True if found, False if not found.
        #
        # Efficiency Note: BST search is often more efficient than linear search because
        # it eliminates half of the remaining tree at each step (on a balanced tree).
        # Instead of scanning every element O(n), it achieves O(log n) time complexity.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # Base Cases: root is null (not found) or key is present at root
        if node is None:
            return False
        if node.value == value:
            return True

        # Value is smaller than root's value, look left
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Value is greater than root's value, look right
        return self._search_recursive(node.right, value)

    def inorder(self):
        # Return a list containing the values from an in-order traversal.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node:
            # Visit the left subtree (all smaller values)
            self._inorder_recursive(node.left, values)

            # Visit the current node
            values.append(node.value)

            # Visit the right subtree (all larger values)
            self._inorder_recursive(node.right, values)

            # Why this produces sorted output:
            # By definition, all values in the left subtree are smaller than the current node,
            # and all values in the right subtree are larger. Processing Left -> Current -> Right
            # guarantees elements are visited in strictly ascending order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")

    # 1. Create a BST object.
    tree = BST()

    # 2. Insert 7 values.
    # Elements are selected to build a balanced tree structure around the root (50).
    inserted_values = [50, 30, 70, 20, 40, 60, 80]
    for val in inserted_values:
        tree.insert(val)

    # 4. Display the values inserted.
    print(f"Inserted values in order: {inserted_values}")
    print("Root element established: 50")

    # 5. Comment on space reduction:
    # Each insertion reduces the search/placement space. For example, inserting '20':
    # - Compared to 50: 20 < 50, so we completely ignore the right subtree (70, 60, 80). Space halved!
    # - Compared to 30: 20 < 30, so we move to its empty left pointer and place it there.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")

    # 1. & 2. Perform and display traversal results.
    sorted_output = tree.inorder()
    print(f"In-order Traversal Result: {sorted_output}")

    # 3. Explanation of sorted output:
    # The traversal recursively fetches the left child first (the absolute minimums),
    # then outputs the parent, then visits the right child. This mirrors the natural
    # left-to-right ascending structure of a valid BST.

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # 1. Search for at least two values that exist.
    print(f"Searching for 40 (Exists): {tree.search(40)}")
    print(f"Searching for 70 (Exists): {tree.search(70)}")

    # 2. Search for at least two values that do not exist.
    print(f"Searching for 15 (Does not exist): {tree.search(15)}")
    print(f"Searching for 99 (Does not exist): {tree.search(99)}")

    # 3. Explanation of results:
    # When searching for 40: 40 < 50 (Go Left), 40 > 30 (Go Right), 40 == 40 (Found! True).
    # When searching for 15: 15 < 50 (Go Left), 15 < 30 (Go Left), 15 < 20 (Go Left -> Hits None, False).

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Demonstration: Operating on an Empty Tree
    empty_tree = BST()
    print(f"Traversing an empty tree: {empty_tree.inorder()}")
    print(f"Searching an empty tree for 50: {empty_tree.search(50)}")

    # Explanation:
    # In an empty tree, `self.root` is initialized to `None`.
    # - The traversal gracefully returns an empty list because the initial `if node:` check fails.
    # - The search gracefully returns `False` immediately because `if node is None:` base case triggers.
    # This prevents the program from throwing `AttributeError` exceptions.


if __name__ == "__main__":
    main()
