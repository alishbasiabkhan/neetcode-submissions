from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seenChars = Counter()
        longestSubstringLen = 0

        for right in range(len(s)):
            seenChars[s[right]] += 1
            while seenChars[s[right]] > 1:
                seenChars[s[left]] -= 1
                left += 1
            longestSubstringLen = max(longestSubstringLen, right - left + 1)
        return longestSubstringLen
        
                