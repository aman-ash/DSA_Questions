class Solution:
    def canTransform(self, S1, S2):
        S1_dic = {}
        if len(S1) != len(S2):
            return 0

        for i in range(len(S1)):
            if S1[i] not in S1_dic:
                S1_dic[i] = 1
            else:
                S1_dic[i] += 1

        for i in range(len(S2)):
            if S2[i] in S1_dic:
                S1_dic[i] -= 1
            else:
                return 0

        for key, value in S1_dic.items():
            if key != 0:
                return 0

        return 1


if __name__ == "__main__":
    S = "RXXLRXRXL"
    T = "XRLXXRRLX"
    ob = Solution()
    print(ob.canTransform(S, T))
