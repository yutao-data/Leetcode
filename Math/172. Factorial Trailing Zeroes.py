class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0

        for i in range(5, n + 1, 5):
            current = i

            # using while because 5 target multiple like 25 exists
            while current % 5 == 0:
                zero_count += 1
                current //= 5

        return zero_count