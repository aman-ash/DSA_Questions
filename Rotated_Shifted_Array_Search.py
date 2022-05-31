class Solution:
    def search(self, nums, target):
        
        def Bsearch(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                
                
                if nums[l] <= nums[mid]:
                    if target >= nums[l] and target <= nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                else:
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid + 1
                    else:
            
                        r = mid - 1
            return -1
                        

        return Bsearch(0, len(nums)-1)
    
if __name__ == '__main__':
    ob = Solution()
    arr = [3, 4, 5, 6, 1, 2]
    print(ob.search(arr, 2))
        
                
        