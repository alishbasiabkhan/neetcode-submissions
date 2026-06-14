class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # print(s)
            count = 26 * [0]
            for c in s:
                # print(c)
                count[ord(c) - ord('a')] += 1
                # print(count)
            res[tuple(count)].append(s)
        return(list(res.values()))