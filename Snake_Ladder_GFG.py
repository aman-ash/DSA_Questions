from collections import deque

class Solution:
    def minThrow(self, N, arr):
        d = {arr[i]:arr[i+1] for i in range(0, N , 2)}
        visit = set()
        
        queue = deque()
        queue.append([1, 0])
        
        while queue:
            cell, moves = queue.popleft()
            if cell == 36:
                return moves
            
            if cell in visit:
                continue
            visit.add(cell)
            moves += 1
            
            for i in range(1, 7):
                nextCell = cell + i
                if nextCell in d:
                    nextCell = d[nextCell]
                queue.append([nextCell, moves])
        
        return -1
    
if __name__ == "__main__":
    ob = Solution()
    A = [2, 15, 14, 35, 17, 13]
    print(ob.minThrow(len(A), A))