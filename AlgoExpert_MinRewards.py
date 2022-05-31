class Solution:

    def minRewards(self, scores):
        rewards = [0 for _ in scores]
        minimum = scores[0]
        Idx = 0

        for i in range(1, len(scores)):
            if scores[i] < minimum:
                minimum = scores[i]
                Idx = i
        rewards[Idx] = 1
        i = j = Idx

        while i > 0:
            if scores[i - 1] > scores[i]:
                rewards[i - 1] = rewards[i] + 1
            else:
                rewards[i - 1] = 1
            i -= 1

        while j < len(scores) - 1:
            if scores[j] < scores[j + 1]:
                rewards[j + 1] = rewards[j] + 1
            else:
                rewards[j + 1] = 1
            j += 1

        for i in range(len(rewards) - 1):
            if rewards[i] == rewards[i + 1]:
                j = i + 1
                if scores[i] > scores[j]:
                    for k in range(j, 0, -1):
                        if rewards[k] == rewards[k - 1]:
                            rewards[k - 1] += 1

                if scores[i] < scores[j]:
                    for k in range(j, len(rewards) - 1):
                        if rewards[k] == rewards[k + 1]:
                            rewards[k + 1] += 1

        return sum(rewards)


def main():
    scores = list(map(int, input().strip().split()))
    ob = Solution()
    result = ob.minRewards(scores)
    print(result)


if __name__ == "__main__":
    main()
