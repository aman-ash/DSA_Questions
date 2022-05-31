class Solution:
    def longestBeautifulSubstring(self, word):
        N = len(word)
        vowels = 'aeiou'
        longest = word[0] if word[0] in vowels else 0
        temp = longest
    
        for i in range(1,N):
            NIV = word[i] not in vowels
            NIO = word[i] < word[i-1]
            
            if NIV or NIO:
                if self.isValid(temp):
                    if len(temp) > len(longest):
                        longest = temp
                temp = word[i] if word[i] in vowels else ''
                        
                
            else:
                temp += word[i]
        
        return len(longest)
    
    
    def isValid(self, s):
        vowels = 'aeiou'
        for v in vowels:
            if v not in s:
                return False
        return True
    
    
if __name__ == '__main__':
    ob = Solution()
    s = "aeeeiiiioooauuuaeiou"
    print(ob.longestBeautifulSubstring(s))