class Solution:
    def partitionLabels(self, s):
        lastSeen = {c: i for i, c in enumerate(s)}
        j, anchor = 0, 0

        ans = []
        for i, c in enumerate(s):
            j = max(j, lastSeen[c])

            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


if __name__ == '__main__':
    ob = Solution()
    result = ob.partitionLabels("ababcbacadefegdehijhklij")
    print(result)
