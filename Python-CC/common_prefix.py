"""
find the common prefix in ["flower", "flow", "flight"]

expected output: fl


"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest = ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            if all([x.startswith(shortest[:i + 1]) for x in strs]):
                longest = shortest[:i + 1]
            else:
                break

        return longest