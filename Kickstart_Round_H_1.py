class Solution:
    def func(self, S, F, alphabet):
        ans = [[0 for _ in S] for _ in F]
        for j in range(len(F)):
            for i in range(len(S)):
                temp = abs(int(alphabet[F[j]]) - int(alphabet[S[i]]))
                if temp > 13:
                    temp = 26 - temp
                ans[j][i] = temp
        A = []

        for i in range(len(S)):
            A.append(min(x[i] for x in ans))
        return sum(A)


def main():
    ob = Solution()
    alphabet = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
    }
    t = int(input())
    for case in range(t):
        S = input()
        F = input()
        print('Case #%d: %s' % (case+1, ob.func(S, F, alphabet)))


if __name__ == '__main__':
    main()
