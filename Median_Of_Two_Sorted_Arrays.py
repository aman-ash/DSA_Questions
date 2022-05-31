class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if not nums1 or not nums2:
            self.baseCase(nums1, nums2)

        first = self.getMedian(nums1)
        secound = self.getMedian(nums2)

        return (first + secound) / 2

    def baseCase(self, array1, array2):
        if array1:
            if len(array1) < 2:
                return array1[0]
            return self.getMedian(array1)

        elif array2:
            if len(array2) < 2:
                return array2[0]
            return self.getMedian(array2)

        else:
            return -1

    def getMedian(self, array):
        N = len(array)

        if N % 2 == 0:
            Idx1 = N // 2
            Idx2 = Idx1 - 1
            return (array[Idx1] + array[Idx2]) / 2

        return array[N // 2]


if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    ob = Solution()
    result = ob.findMedianSortedArrays(nums1, nums2)
    print(result)
