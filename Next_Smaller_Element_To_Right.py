class Solution:
    # Next Greater Element in the Right side of Array 
    def nextGreaterElements(self, nums):
        N = len(nums)
        res = [-1 for _ in range(N)]
        stack = [nums[i] for i in reversed(range(N))]
        
        for i in reversed(range(N)):
            curElement = nums[i]
            
            while stack:
                if stack[-1] > curElement:
                    res[i] = stack[-1]
                    break
                else:
                    stack.pop()
                    
            stack.append(curElement)
        
        return res
     
     
    # Next smallest Element in the Right side of Array   
    def nextSmallerElements(self, nums):
        N = len(nums)
        res = [-1 for _ in range(N)]
        stack = []
        
        for i in reversed(range(N)):
            cur = nums[i]
        
            while stack:
                if stack[-1] < cur:
                    res[i] = stack[-1]
                    break
                else:
                    stack.pop()
            
            stack.append(cur)
        return res


    # Next Greater Element in the left side of Array 
    def nearestGreaterToLeft(self, nums):
        N = len(nums)
        res = [-1 for _ in range(N)]
        stack = []
        
        for i, cur in enumerate(nums):
            while stack:
                if stack[-1] > cur:
                    res[i] = stack[-1]
                    break
                else:
                    stack.pop()
            
            stack.append(cur)
        return res


    # Next smallest Element in the left side of Array 
    def nearestSmallerToLeft(self, nums):
        N = len(nums)
        res = [-1 for _ in range(N)]
        stack = []
        
        for i, cur in enumerate(nums):
            while stack:
                if stack[-1] < cur:
                    res[i] = stack[-1]
                    break
                else:
                    stack.pop()
            
            stack.append(cur)
        return res



if __name__ == '__main__':
    ob = Solution()
    nums = [1,4,3,2,7,6]
    print(ob.nearestSmallerToLeft(nums))