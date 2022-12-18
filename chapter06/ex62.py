from __future__ import annotations


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    c.sort()

    ans = 0
    for e in b:
        ans += lower_bound(a, e) * (n - upper_bound(c, e))
    print(ans)


def lower_bound(lst: list[int], key: int) -> int:
    left: int = 0
    right: int = len(lst) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if lst[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1


def upper_bound(lst: list[int], key: int) -> int:
    left: int = 0
    right: int = len(lst) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if lst[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1


if __name__ == "__main__":
    main()
