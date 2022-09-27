def main():
    N: int = int(input())
    h: list[int] = list(map(int, input().split(" ")))

    dp: list[int] = [10000000000] * N
    dp[0] = 0
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[N - 1])


if __name__ == "__main__":
    main()
