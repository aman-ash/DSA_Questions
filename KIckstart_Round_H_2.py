class Solution:
    def func(self, P, colors, combinations):
        stroke = 1
        temp = colors[P[0]]
        for i in range(len(P)):
            if colors[P[i]] in combinations:
                if colors[P[i]] != temp:
                    j = self.getIndex(i, P)
                    N = self.getvalue(i, j, P, colors, combinations)
                    stroke += N
                    temp = colors[P[i]]

            elif colors[P[i]] != temp:
                if colors[P[i - 1]] in combinations:
                    if colors[P[i]] in combinations[colors[P[i - 1]]]:
                        temp = colors[P[i]]
                        continue
                stroke += 1
                temp = colors[P[i]]

        return stroke

    def getvalue(self, i, j, P, colors, combinations):
        A = 0

        if colors[P[j]] in combinations[colors[P[i]]]:
            A = len(combinations[colors[P[i]]]) - 1
        else:
            len(combinations[colors[P[i]]])
        return A

    def getIndex(self, i, P):
        k = i
        while k >= 0:
            if P[k] != P[i]:
                break
            k -= 1
        return k


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        N = int(input())
        P = str(input())
        colors = {'U': 'Uncolored',
                  'R': 'Red',
                  'Y': 'Yellow',
                  'B': 'Blue',
                  'O': 'Orange',
                  'P': 'Purple',
                  'G': 'Green',
                  'A': 'Gray'}
        combinations = {'Orange': ['Red', 'Yellow'],
                        'Purple': ['Red', 'Blue'],
                        'Green': ['Blue', 'Yellow'],
                        'Gray': ['Red', 'Yellow', 'Green'], }
        print('Case #%d: %s' % (case+1, ob.func(P, colors, combinations)))


if __name__ == '__main__':
    main()
