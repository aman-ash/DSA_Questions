class Solution:
    def Anagrams(self, words):
        ana = {}

        for word in words:
            temp = word
            word = sorted(word)
            word = ''.join(word)

            if word in ana:
                ana[word].append(temp)

            else:
                ana[word] = [temp]

        return list(ana.values())


if __name__ == '__main__':
    words = ['act', 'god', 'cat', 'dog', 'tac']
    ob = Solution()
    print(ob.Anagrams(words))
