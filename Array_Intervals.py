class Solution:
    def insertInterval(self, intervals, I):
        answer = []
        swap = False
        for interval in intervals:
            if answer:
                I = answer[-1]

            if I[0] <= interval[0] and I[0] >= interval[1]:
                newInterval = [min(interval[0], I[0]), max(interval[1], I[1])]
                swap = True

            else:
                newInterval = interval

            if newInterval not in answer:
                answer.append(newInterval)

        if not swap:
            answer.append(I)

        return answer


def main():
    ob = Solution()
    N = int(input())
    intervals = [list(map(int, input().split())) for _ in range(N)]
    I = list(map(int, input().split()))
    answer = ob.insertInterval(intervals, I)
    print(answer)


if __name__ == "__main__":
    main()
