def maxValueK(A):
    N = len(A)
    A.sort()
    answer = 0
    for i in range(N):
        cur = A[i]
        count = N - (i+1)
        if count >= cur:
            if cur > answer:
                answer = cur

    return


if __name__ == "__main__":
    A = [10, 10]
    print(maxValueK(A))
