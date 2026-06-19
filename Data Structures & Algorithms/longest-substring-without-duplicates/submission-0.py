class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstringLen = 0
        seenChars = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1
            seenChars.add(s[right])
            longestSubstringLen = max(longestSubstringLen, right - left + 1)
            # print(seenChars) 

        return longestSubstringLen
        
                