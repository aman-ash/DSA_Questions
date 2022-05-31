from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        N = len(board)
        board.reverse()
        for i in range(1, N, 2):
            board[i].reverse()
            
        def get():
            T = {}
            for i in range(N):
                for j in range(N):
                    cur = i * N + j + 1
                    if board[i][j] != -1:
                        T[cur] = board[i][j]
            return T
        
        d = get()
        visit = set()
        queue = deque()
        queue.append([1, 0])
        
        while queue:
            cell, moves = queue.popleft()
            if cell == N*N:
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
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    print(ob.snakesAndLadders(board))