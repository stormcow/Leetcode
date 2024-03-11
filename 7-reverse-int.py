class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        is_negative = x < 0
        x = abs(x)
        while x > 0:
            rightmost_digit = x % 10 
            reversed_x = (reversed_x * 10) + rightmost_digit
            x = x // 10

        if int.bit_length(reversed_x) >= 32:
            return 0

        return -reversed_x if is_negative else reversed_x
