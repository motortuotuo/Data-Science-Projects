def solution(N, K):
    # write your code in Python 3.6
    min_moves = 0
    double_counts =0

    if N == 1:
        return 0

    while True:
        if N%2==0 and K>double_counts:
            N=N/2
            double_counts +=1
            min_moves +=1
        else:
            N=N-1
            min_moves+=1
        print(N)
        if N==1:
            break
    return min_moves
min_moves = solution(18, 2)
print(min_moves)