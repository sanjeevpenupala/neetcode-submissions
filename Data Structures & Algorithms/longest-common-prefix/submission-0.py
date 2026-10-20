class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        columns = list(zip(*strs))
        ans = ""

        for chars in columns:
            if len(set(chars)) != 1:
                return ans
            ans += chars[0]

        return ans          