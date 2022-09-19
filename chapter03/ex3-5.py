def main():
    N: int = int(input())
    A: list[int] = list(map(int, input().split()))

    cnt: int = 0
    while True:
        flag: bool = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                flag = False

        if flag:
            cnt += 1
        else:
            break

    print(cnt)


if __name__ == "__main__":
    main()
