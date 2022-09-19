def main():
    lst = list(map(int, input().split()))
    K: int = lst[0]
    S: int = lst[1]

    cnt: int = 0
    for i in range(K + 1):
        for j in range(K + 1):
            if 0 <= S - i - j <= K:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
