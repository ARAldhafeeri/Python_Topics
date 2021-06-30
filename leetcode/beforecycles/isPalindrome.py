
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        ans = ''
        for i in s:
            if i.isalnum():
                ans +=i.lower()

        return ans == ans[::-1]
