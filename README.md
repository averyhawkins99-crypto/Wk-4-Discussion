# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

The design process involved designing a system that was simple and object-oriented with the help of a Node class for data management and a BST class for tree management. In this way, the code will mimic the structure of the binary search tree, since the structure of the node will be separated from the tree structure. Recursive helper functions have been used to handle tasks such as insertion, search, and traversal. The program clearly depicts a BST based on a key insertion process that is balanced (with root 50 and keys 30, 70, 20, 40, 60, 80). If a user is searching for an existing key (e.g., 40) or an inexistent one (e.g., 15), the program illustrates the essence of a binary search tree by checking the value of the present node and moving either entirely to the left or entirely to the right.

• Improvements in Performance: Trees basically provide improved performance for lookup, insertion, and deletion. As against a regular array or list, where the operation involves looking at each element once in (O(n)) linear time, a balanced BST arranges its data in such a manner that lookups are done in (O(logn)) logarithmic time. The comparisons made at every step reduce the rest of the job by half.
• How BSTs Can Turn Out To Be Inefficient: A regular BST is not balanced by itself. If entries are made in an increasing or almost increasing order (like 20, 30, 40, 50), the BST gets reduced to a completely unbalanced linked list. This is the worst case when the height of the tree becomes equal to the number of entries ((h = n)).   

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
