class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreqs = {}
        for ch in t:
            tFreqs[ch] = 1 + tFreqs.get(ch, 0)

        sFreqs = {}
        count = 0
        res = ''
        curMin = float('inf')
        l = 0
        for r in range(len(s)):
            if s[r] in tFreqs:
                sFreqs[s[r]] = 1 + sFreqs.get(s[r], 0)
                if sFreqs[s[r]] <= tFreqs[s[r]]:
                    count += 1
            
            while count == len(t):
                curWindow = r - l + 1
                if curWindow < curMin:
                    curMin = curWindow
                    res = s[l:r + 1]
                if s[l] in tFreqs:
                    sFreqs[s[l]] -= 1
                    if sFreqs[s[l]] < tFreqs[s[l]]:
                        count -= 1
                l += 1
        return res