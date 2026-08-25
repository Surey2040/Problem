import json

titles = [
    "Two Sum", "Add Two Numbers", "Longest Substring Without Repeating Characters", "Median of Two Sorted Arrays",
    "Longest Palindromic Substring", "Zigzag Conversion", "Reverse Integer", "String to Integer (atoi)",
    "Palindrome Number", "Regular Expression Matching", "Container With Most Water", "Integer to Roman",
    "Roman to Integer", "Longest Common Prefix", "3Sum", "3Sum Closest", "Letter Combinations of a Phone Number",
    "4Sum", "Remove Nth Node From End of List", "Valid Parentheses", "Merge Two Sorted Lists",
    "Generate Parentheses", "Merge k Sorted Lists", "Swap Nodes in Pairs", "Reverse Nodes in k-Group",
    "Remove Duplicates from Sorted Array", "Remove Element", "Find the Index of the First Occurrence in a String",
    "Divide Two Integers", "Substring with Concatenation of All Words", "Next Permutation",
    "Longest Valid Parentheses", "Search in Rotated Sorted Array", "Find First and Last Position of Element in Sorted Array",
    "Search Insert Position", "Valid Sudoku", "Sudoku Solver", "Count and Say", "Combination Sum",
    "Combination Sum II", "First Missing Positive", "Trapping Rain Water", "Multiply Strings",
    "Wildcard Matching", "Jump Game II", "Permutations", "Permutations II", "Rotate Image",
    "Group Anagrams", "Pow(x, n)", "N-Queens", "N-Queens II", "Maximum Subarray", "Spiral Matrix",
    "Jump Game", "Merge Intervals", "Insert Interval", "Length of Last Word", "Spiral Matrix II",
    "Permutation Sequence", "Rotate List", "Unique Paths", "Unique Paths II", "Minimum Path Sum",
    "Valid Number", "Plus One", "Add Binary", "Text Justification", "Sqrt(x)", "Climbing Stairs",
    "Simplify Path", "Edit Distance", "Set Matrix Zeroes", "Search a 2D Matrix", "Sort Colors",
    "Minimum Window Substring", "Combinations", "Subsets", "Word Search", "Remove Duplicates from Sorted Array II",
    "Search in Rotated Sorted Array II", "Remove Duplicates from Sorted List II", "Remove Duplicates from Sorted List",
    "Largest Rectangle in Histogram", "Maximal Rectangle", "Partition List", "Scramble String",
    "Merge Sorted Array", "Gray Code", "Subsets II", "Decode Ways", "Reverse Linked List II",
    "Restore IP Addresses", "Binary Tree Inorder Traversal", "Unique Binary Search Trees II",
    "Unique Binary Search Trees", "Interleaving String", "Validate Binary Search Tree",
    "Recover Binary Search Tree", "Same Tree", "Symmetric Tree", "Binary Tree Level Order Traversal",
    "Binary Tree Zigzag Level Order Traversal", "Maximum Depth of Binary Tree", "Construct Binary Tree from Preorder and Inorder Traversal",
    "Construct Binary Tree from Inorder and Postorder Traversal", "Binary Tree Level Order Traversal II",
    "Convert Sorted Array to Binary Search Tree", "Convert Sorted List to Binary Search Tree",
    "Balanced Binary Tree", "Minimum Depth of Binary Tree", "Path Sum", "Path Sum II", "Flatten Binary Tree to Linked List",
    "Distinct Subsequences", "Populating Next Right Pointers in Each Node", "Populating Next Right Pointers in Each Node II",
    "Pascal's Triangle", "Pascal's Triangle II", "Triangle", "Best Time to Buy and Sell Stock",
    "Best Time to Buy and Sell Stock II", "Best Time to Buy and Sell Stock III", "Binary Tree Maximum Path Sum",
    "Valid Palindrome", "Word Ladder II", "Word Ladder", "Longest Consecutive Sequence", "Sum Root to Leaf Numbers",
    "Surrounded Regions", "Palindrome Partitioning", "Palindrome Partitioning II", "Clone Graph",
    "Gas Station", "Candy", "Single Number", "Single Number II", "Copy List with Random Pointer",
    "Word Break", "Word Break II", "Linked List Cycle", "Linked List Cycle II", "Reorder List",
    "Binary Tree Preorder Traversal", "Binary Tree Postorder Traversal", "LRU Cache", "Insertion Sort List"
]

problems = []
for title in titles:
    problems.append({
        "title": title,
        "difficulty": "Medium",
        "code": f"class Solution:\n    def solve_{title.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '')}(self):\n        pass"
    })

with open("d:/our site/Problem_repo/problems.json", "w") as f:
    json.dump(problems, f, indent=4)
