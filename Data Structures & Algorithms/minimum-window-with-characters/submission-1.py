class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or  (len(t) > len(s)):
            return("")

        setT, currentWindow = {}, {}
        for c in t:
            setT[c] = 1 + setT.get(c, 0)

        have, need = 0, len(setT)
        result = [-1, -1]
        resultLength = float('inf')
        left = 0

        for right in range(len(s)):
            currentWindow[s[right]] = 1 + currentWindow.get(s[right], 0)
            if s[right] in setT and currentWindow[s[right]] == setT[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLength:
                    result = [left, right]
                    resultLength = right - left + 1
                currentWindow[s[left]] -= 1
                if s[left] in setT and currentWindow[s[left]] < setT[s[left]]:
                    have -= 1
                left += 1
            # print('have:', have, 'need:', need, 'currentWindow:', currentWindow)

        if resultLength != float('inf'):
            left, right = result
        else:
            return ""
        # print('result:', s[left:right+1])

        return s[left:right+1]

        