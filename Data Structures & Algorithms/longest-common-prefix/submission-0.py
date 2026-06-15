class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #pick 1st word as prefix and keep comparing
        # with rest of the words, if any mismatch shrink the prefix 
        commonPrefix = strs[0]
        for i in range(1,len(strs)):
            j = 0
            while j < min(len(strs[i]), len(commonPrefix)):
                if strs[i][j] != commonPrefix[j]:
                    break
                j += 1
            commonPrefix = commonPrefix[:j]
            print(commonPrefix)

        return commonPrefix
        