cnt: int = 0


def calc753(n: int, num: int):
    # numが入力されたN以下で、3,5,7すべてを含む場合は答えをインクリメント
    # numがNより大きい場合はreturn
    if num <= n and "3" in str(num) and "5" in str(num) and "7" in str(num):
        global cnt
        cnt += 1
    elif num > n:
        return

    calc753(n, 10 * num + 7)
    calc753(n, 10 * num + 5)
    calc753(n, 10 * num + 3)


def main():
    N: int = int(input())
    calc753(N, 7)
    calc753(N, 5)
    calc753(N, 3)

    global cnt
    print(cnt)


if __name__ == "__main__":
    main()
