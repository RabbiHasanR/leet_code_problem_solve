class Solution:

    def decimal_to_binary_base_n(self, decimal_number, base):
        if decimal_number == 0:
            return '0'
        binary = ''
        while decimal_number > 0:
            reminder = decimal_number % base
            binary += str(reminder)
            decimal_number //= base
        return binary

    def isStrictlyPalindromic(self, n: int) -> bool:

        for base in range(2, n-1):
            binary = self.decimal_to_binary_base_n(n, base)
            temp = binary[::-1]
            if binary != temp:
                return False
        return True