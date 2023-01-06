import heapq
import sys

sys.stdin = open("input_H-index.txt")


def h_index(n: int, citations: list):
    minH = []
    ans = []
    hindex = 0
    for i in range(n):
        if citations[i] > hindex:
            heapq.heappush(minH, citations[i])
        while minH and minH[0] <= hindex:
            heapq.heappop(minH)
        if len(minH) >= hindex + 1:
            hindex += 1
        ans.append(hindex)
    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())  # The number of papers
        citations = [int(s) for s in input().split()]  # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
