def main():
    S: str = input()

    total: int = 0
    # +が入るパターンを全探索
    for bit in range(1 << (len(S) - 1)):
        tmp_sum: int = 0
        for i, e in enumerate(S):
            tmp_sum = tmp_sum * 10 + int(e)
            # パターンで1が立っている場合は+が入ったと仮定して、tmp_sumをtotalに足してリセット
            if bit & (1 << i):
                total += tmp_sum
                tmp_sum = 0
        total += tmp_sum

    print(total)


if __name__ == "__main__":
    main()
