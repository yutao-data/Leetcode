class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            # set all the nines at the end to 0
            if digits[idx] == 9:
                digits[idx] = 0

            # return first un-nine digit
            else:
                digits[idx] += 1
                return digits

        # if all the digits are nines
        return [1] + digits
