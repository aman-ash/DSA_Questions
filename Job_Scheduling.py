class Solution:
    def func(self, jobs):
        jobs = sorted(jobs, key=lambda x:x[1], reverse=True)
        profitArray = [-1 for _ in jobs]
        for i, p in jobs:
            if profitArray[i - 1] == -1:
                profitArray[i - 1] = p
            else:
                Idx = i
                while Idx > 0:
                    if profitArray[Idx - 1] == -1:
                        profitArray[Idx - 1] = p
                        break
                    Idx -= 1

        return sum([x for x in profitArray if x != - 1])
    
    
if __name__ == '__main__':
    ob = Solution()
    A = [1,1,2,2,3]
    profit = [25, 29, 100, 27, 15]
    new = [[A[i], profit[i]] for i in range(len(A))]
    print(ob.func(new))
    