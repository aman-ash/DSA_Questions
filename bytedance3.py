class Solution:
    def fullJustify(self, words, maxWidth):
        length = [len(word) for word in words]
        ans = []

        i = 0
        while i < len(length):
            temp = 0
            count = 0
            no_of_words = 0

            for k in range(i, len(length)):
                temp += length[k]
                count += 1
                no_of_words += 1

                if temp + count > maxWidth:
                    count -= 1
                    if temp + count > maxWidth:
                        temp -= length[k]
                        count -= 1
                        no_of_words -= 1

                    break

            if no_of_words + i == len(words):
                current = ''
                space = ' '
                diff = maxWidth - temp - no_of_words + 1
                for j in range(i, i + no_of_words):
                    current += words[j]
                    if j == len(words) - 1:
                        break
                    current += space

                current += space * diff
                ans.append(current)
                i += no_of_words
                continue

            if no_of_words == 1:
                spaces = maxWidth - temp
                current = ''
                diff = maxWidth - temp

                current += words[i]
                current += diff * ' '

            else:
                spaces = (maxWidth - temp) // (no_of_words - 1)
                space = spaces * ' '
                current = ''
                diff = maxWidth - (temp + (spaces * (no_of_words - 1)))
                for j in range(i, i + no_of_words):
                    current += words[j]
                    if j == i:
                        current += ' ' * diff
                    if len(current) == maxWidth:
                        break

                    current += space

            ans.append(current)
            i += no_of_words

        return ans


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
             "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    ob = Solution()
    result = ob.fullJustify(words, 20)
    print(result)
