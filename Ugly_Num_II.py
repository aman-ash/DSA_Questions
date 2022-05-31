class Solution:
    def nthUglyNumber(self, i: int):
        nums = set()
        nums.add(1)
        seen = set()
        
        while len(nums) <= i:
            temp = nums.copy()
            for n in nums:
                if n in seen:
                    continue
                seen.add(n)
                temp.add(n*2)
                temp.add(n*3)
                temp.add(n*5)
            nums = temp.copy()
            
        nums = list(nums)
        nums.sort()
        print(nums)
        return nums[i - 1]
                
    
    
    
    
if __name__ == "__main__":
    ob = Solution()
    print(ob.nthUglyNumber(9))