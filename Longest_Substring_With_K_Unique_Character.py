class Solution:
    
    def longestKSubstr(self, s, k):
        d = {} 
        i = j = 0
        ans = -1
        
        def add(w):
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
            return
        
        while j < len(s):
            add(s[j])
            
            if len(d) == k:
                cur = j - i + 1
                ans = max(ans, cur)
            
            elif len(d) > k:
                while len(d) > k:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i += 1
            
            j += 1
        
        return ans
            
             
    
    
    
if __name__ == '__main__':
    ob = Solution()
    s = 'aabacaaabebebe'
    print(ob.longestKSubstr(s, 3))