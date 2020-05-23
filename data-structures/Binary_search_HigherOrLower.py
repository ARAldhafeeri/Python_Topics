"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower."""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while (left <= right):
            mid = left + (right - left) // 2
            res = guess(mid)
            if (res == 0):
                return mid
            # if number higer then go to the right
            elif (res == 1):
                left = mid + 1
            # if number is lower then go to the left
            else:
                right = mid - 1

        return -1


