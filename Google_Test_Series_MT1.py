class Solution:
    def goodNumsInRange(self, l, r):
        answer = []
        combination1 = {'0', '1', '8'}
        combination2 = {'6', '9'}
        rotated = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        if r <= 10:
            for i in range(l, r):
                if str(i) in combination2:
                    answer.append(i)

            return answer

        if l <= 9:
            if l <= 6:
                answer.append(6)
            answer.append(9)

        for i in range(l, r):
            current = str(i)
            rotate = ''
            InCombi1 = False
            InCombi2 = False
            for s in current:
                if s in combination1:
                    InCombi1 = True
                    rotate += rotated[s]
                if s in combination2:
                    InCombi2 = True
                    rotate += rotated[s]

            if InCombi1 and InCombi2:
                if rotate:
                    if int(rotate) >= l and int(rotate) <= r and int(rotate) not in answer:
                        answer.append(int(rotate))

        return answer


def main():
    ob = Solution()
    l, r = map(int, input().split())
    ans = ob.goodNumsInRange(l, r)
    if not ans:
        print(-1)
    print(*ans)


if __name__ == '__main__':
    main()
