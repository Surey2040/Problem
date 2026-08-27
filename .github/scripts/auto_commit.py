import os
import random
import subprocess
import time
from datetime import datetime

# =================================================================
# 1. REPO PATH A MAATHUNGA (CHANGE THIS PATH)
# Neenga entha repo-la push pannanumo antha folder path-a inga podunga
# Example: r"C:\Users\surey\Documents\GitHub\Problem"
# =================================================================
REPO_PATH = "." 

# =================================================================
# 2. GREEN COLOR CONTROL (RANDOM COMMITS PER DAY)
# Mid-green and Dark-green (Level 2 & 3) varathukku 4 to 9 commits thevai.
# Ithu daily random ah oru number eduthukum, so color um random ah maarum!
# =================================================================
MIN_COMMITS = 4
MAX_COMMITS = 9


# -----------------------------------------------------------------
# 3. REALISTIC CODE TEMPLATES (JAVA & PYTHON)
# Intha code thaan real-a push aagum. Title mattum illa, actual program irukum!
# -----------------------------------------------------------------
PROBLEMS = [
    {
        "filename": "TwoSum.java",
        "message": "Add optimal solution for TwoSum",
        "code": """public class TwoSum {\n    public int[] twoSum(int[] nums, int target) {\n        java.util.Map<Integer, Integer> map = new java.util.HashMap<>();\n        for (int i = 0; i < nums.length; i++) {\n            int complement = target - nums[i];\n            if (map.containsKey(complement)) {\n                return new int[] { map.get(complement), i };\n            }\n            map.put(nums[i], i);\n        }\n        return new int[]{};\n    }\n}"""
    },
    {
        "filename": "BinarySearch.java",
        "message": "Implement Binary Search algorithm",
        "code": """public class BinarySearch {\n    public int search(int[] nums, int target) {\n        int left = 0, right = nums.length - 1;\n        while (left <= right) {\n            int mid = left + (right - left) / 2;\n            if (nums[mid] == target) return mid;\n            if (nums[mid] < target) left = mid + 1;\n            else right = mid - 1;\n        }\n        return -1;\n    }\n}"""
    },
    {
        "filename": "PalindromeCheck.java",
        "message": "Add Palindrome check utility",
        "code": """public class PalindromeCheck {\n    public boolean isPalindrome(String s) {\n        int left = 0, right = s.length() - 1;\n        while (left < right) {\n            if (s.charAt(left) != s.charAt(right)) return false;\n            left++;\n            right--;\n        }\n        return true;\n    }\n}"""
    },
    {
        "filename": "ReverseLinkedList.java",
        "message": "Fix edge case in Reverse Linked List",
        "code": """class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\npublic class ReverseLinkedList {\n    public ListNode reverseList(ListNode head) {\n        ListNode prev = null;\n        ListNode curr = head;\n        while (curr != null) {\n            ListNode nextTemp = curr.next;\n            curr.next = prev;\n            prev = curr;\n            curr = nextTemp;\n        }\n        return prev;\n    }\n}"""
    },
    {
        "filename": "fibonacci.py",
        "message": "Add dynamic programming approach for Fibonacci",
        "code": """def fibonacci(n):\n    if n <= 1:\n        return n\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i-1] + dp[i-2]\n    return dp[n]\n\nif __name__ == '__main__':\n    print(fibonacci(10))\n"""
    },
    {
        "filename": "valid_parentheses.py",
        "message": "Solve Valid Parentheses using stack",
        "code": """def isValid(s):\n    stack = []\n    mapping = {")": "(", "}": "{", "]": "["}\n    for char in s:\n        if char in mapping:\n            top_element = stack.pop() if stack else '#'\n            if mapping[char] != top_element:\n                return False\n        else:\n            stack.append(char)\n    return not stack\n"""
    },
    {
        "filename": "merge_intervals.py",
        "message": "Optimize merge intervals sorting",
        "code": """def merge(intervals):\n    intervals.sort(key=lambda x: x[0])\n    merged = []\n    for interval in intervals:\n        if not merged or merged[-1][1] < interval[0]:\n            merged.append(interval)\n        else:\n            merged[-1][1] = max(merged[-1][1], interval[1])\n    return merged\n"""
    }
]

# Random commit message variations to make it look 100% natural
VERBS = ["Update", "Refactor", "Clean up code in", "Optimize", "Fix minor issues in"]

def run_cmd(cmd):
    # Run the git commands in the repository folder
    result = subprocess.run(cmd, shell=True, cwd=REPO_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    run_cmd('git config --global user.name "GitHub Actions Bot"')
    run_cmd('git config --global user.email "actions@github.com"')
    if not os.path.exists(REPO_PATH):
        print(f"Error: Path {REPO_PATH} does not exist. Please edit the python file and set the correct REPO_PATH.")
        return

    # Pick a random number of commits between 4 and 9
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Planning to make {num_commits} commits today...")

    for i in range(num_commits):
        # Pick a random problem (Java or Python)
        problem = random.choice(PROBLEMS)
        filepath = os.path.join(REPO_PATH, problem["filename"])
        
        # Add a unique timestamp comment at the end so Git recognizes it as a modified file
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        comment_symbol = "//" if problem["filename"].endswith(".java") else "#"
        unique_comment = f"\n{comment_symbol} Code update: {timestamp}\n"
        
        # Write real code + unique comment into the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(problem["code"] + unique_comment)
            
        # Determine the commit message dynamically
        if random.random() > 0.5:
            # E.g., "Refactor TwoSum.java"
            commit_msg = f"{random.choice(VERBS)} {problem['filename']}"
        else:
            # E.g., "Add optimal solution for TwoSum"
            commit_msg = problem["message"]
            
        # Git Add
        run_cmd(f'git add "{problem["filename"]}"')
        
        # Git Commit
        run_cmd(f'git commit -m "{commit_msg}"')
        
        print(f"  -> Committed: {commit_msg}")
        
        # Sleep for a few seconds so commit times are slightly different
        time.sleep(random.randint(1, 3))

    print("Pushing to GitHub...")
    # Push to main or master
    if run_cmd('git push origin main'):
        print("Success! Pushed to main branch.")
    elif run_cmd('git push origin master'):
         print("Success! Pushed to master branch.")
    else:
         print("Failed to push. Check your Git connection or branch name.")

if __name__ == "__main__":
    main()
