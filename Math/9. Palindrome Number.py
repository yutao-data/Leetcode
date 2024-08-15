class Solution:
    def isPalindrome(self, x: int) -> bool:
        # handle special cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # get the first half part number and reversed last part number
        reverseNumber = 0
        while x > reverseNumber:
            reverseNumber = reverseNumber * 10 + x % 10
            x //= 10

        # sometimes when the reversed number is odd, just ignore the number in the middle
        return x == reverseNumber or x == reverseNumber // 10