class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for item in s:
            if item in '({[':
                stack.append(item)

            else:
                if stack:
                    current_item = stack.pop()
                    if current_item == '(':
                        if item != ")":
                            return False
                    if current_item == '{':
                        if item != '}':
                            return False
                    if current_item == '[':
                        if item != ']':
                            return False
        if len(stack) > 0:
            return False
        else:
            return True

if __name__ == '__main__':
    s = str(input())
    a = Solution()
    print(a.isValid(s))