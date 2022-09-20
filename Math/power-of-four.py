# first solution
# time: O(logn)


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0 and n % 4 == 0:
            n /= 4
        return n == 1