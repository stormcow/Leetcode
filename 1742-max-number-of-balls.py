class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        balls = {}
        for n in range(lowLimit, highLimit + 1):
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit
                n //= 10
            balls[str(sum)] = balls.get(str(sum), 0) + 1
        return max(balls.values())
