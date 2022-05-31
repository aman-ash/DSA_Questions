class Solution:
    def findIntegers(self, n: int) -> int:
        binaryForm = [bin(i).replace("0b", "") for i in range(n + 1)]
        count = n + 1

        for b in binaryForm:
            for i in range(0, len(b) - 1):
                if b[i] == '1' and b[i + 1] == '1':
                    count -= 1
                    break

        return count


if __name__ == "__main__":
    ob = Solution()
    print(ob.findIntegers(5))
