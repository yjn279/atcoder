def main(h, w, a):
    """
    >>> main(4, 3, [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ...     [10, 11, 12]
    ... ])
    1 4 7 10
    2 5 8 11
    3 6 9 12
    >>> main(2, 2, [
    ...     [1000000000, 1000000000],
    ...     [1000000000, 1000000000]
    ... ])
    1000000000 1000000000
    1000000000 1000000000
    >>> main(1, 1, [
    ...     [1]
    ... ])
    1
    >>> main(1, 2, [
    ...     [1, 2]
    ... ])
    1
    2
    >>> main(2, 1, [
    ...     [1],
    ...     [2]
    ... ])
    1 2
    """


    b = zip(*a)  # 転置
    _ = [print(*b_j) for b_j in b]


if __name__ == '__main__':
    h, w = map(int, input().split())
    a = [[int(j) for j in input().split()] for _ in range(h)]
    main(h, w, a)
