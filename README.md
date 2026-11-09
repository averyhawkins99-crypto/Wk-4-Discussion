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

The real-world scenario modeled in this implementation is a database indexing and rapid-lookup system, using numbers to represent unique tracking records.

The design process involved designing a system that was simple and object-oriented with the help of a Node class for data management and a BST class for tree management. In this way, the code will mimic the structure of the binary search tree, since the structure of the node will be separated from the tree structure. Recursive helper functions have been used to handle tasks such as insertion, search, and traversal. The program clearly depicts a BST based on a key insertion process that is balanced (with root 50 and keys 30, 70, 20, 40, 60, 80). If a user is searching for an existing key (e.g., 40) or an inexistent one (e.g., 15), the program illustrates the essence of a binary search tree by checking the value of the present node and moving either entirely to the left or entirely to the right.

• Improvements in Performance: Trees basically provide improved performance for lookup, insertion, and deletion. As against a regular array or list, where the operation involves looking at each element once in (O(n)) linear time, a balanced BST arranges its data in such a manner that lookups are done in (O(logn)) logarithmic time. The comparisons made at every step reduce the rest of the job by half.
• How BSTs Can Turn Out To Be Inefficient: A regular BST is not balanced by itself. If entries are made in an increasing or almost increasing order (like 20, 30, 40, 50), the BST gets reduced to a completely unbalanced linked list. This is the worst case when the height of the tree becomes equal to the number of entries ((h = n)).   

With regards to edge cases testing, a tree that has no nodes at all was utilized.
The program made an entire new tree (empty_tree = BST()) whereby self.root = None, and does the following:
1. In-order traversal of the empty tree (.inorder()) to confirm whether it will indeed return an empty list [] and not fail.
2. Searches for values on the empty tree (.search(50)) and confirms whether it will return false.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

Completing this Python assignment deepened my understanding of&nbsp;Binary Search Trees (BSTs) and algorithmic traversal mechanics. I gained practical skills in transforming abstract data structures into functional object-oriented code, utilizing a Node class to manage tree pointers. I mastered designing recursive helper methods to handle tree insertion, search, and in-order traversal workflows

The major problem that arose was that of handling empty trees without generating any AttributeError exceptions. I resolved this problem by creating structural base cases whereby I would check whether node is None before attempting to call any attributes such as .left and .right. This made it possible for the empty tree to return either False or an empty list.

For the BST data structure, the ordering is critical and strictly follows a particular rule whereby all the elements that are part of the left subtree are smaller than the current element, whereas those that are part of the right subtree are bigger. The above-mentioned ordering brings about great efficiency when compared to linear data structures such as the usual array or list, which need (O(n)) operations to perform their searches. Due to the way it works, a balanced BST cuts down the search time to (O(logn)).
