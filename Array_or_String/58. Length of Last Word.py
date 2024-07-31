class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])


"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        while p >= 0 and s[p] == " ":
            p -= 1

        length = 0
        while p >= 0 and s[p] != " ":
            p -= 1
            length += 1
        return length
"""