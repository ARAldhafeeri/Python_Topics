"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            # get unicode of letter using ord() -> letters to unicode
            # 0 xor 0 = 0, 1 xor 1 = 0, 1 xor 0 = 1, 0 xor 1 = 0
            # xor dublicate to cancle them a^a = 0, 0^b = b
            diff ^= ord(s[i])
            diff ^= ord(t[i])
        diff ^= ord(t[len(t) -1 ])
        return chr(diff)
            