class Solution:
    def func(self):
        return "Hello World!"


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        print('Case #%d: %s' % (case+1, ob.func()))


if __name__ == '__main__':
    main()
