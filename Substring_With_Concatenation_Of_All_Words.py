class Solution:
    def findSubstring(self, s , words):
        word = ''
        for w in words:
            word += w
        
        word = sorted(word)
        res = []
        
        i, j, N, K = 0, 0, len(s),len(word)
        
        while j < N:
            if (j - i + 1) < K:
                j += 1
            
            else:
                new = sorted(s[i:j+1])
                if new == word:
                    res.append(i)
                
                i += 1
        
        return res
    

if __name__ == "__main__":
    ob = Solution()
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(ob.findSubstring(s, words))