class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            # Sort the characters of the string to create a key.
            ans[tuple(sorted(s))].append(s)
        return ans.values()