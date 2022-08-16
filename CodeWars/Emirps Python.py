def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2:
        return
    yield 2
    f = [True] * n
    seq1 = range(3, int(n ** 0.5), 2)
    seq2 = range(seq1[-1] + 2, n, 2)
    for p in filter(f.__getitem__, seq1):
        yield p
        for q in range(p * p, n, 2 * p):
            f[q] = False
    for p in filter(f.__getitem__, seq2):
        yield p


def find_emirp(n):
    lst = [p for i, p in zip(range(n), primes_up_to(n))]
    lst = [p for i, p in
           zip(range(max([int(str(x)[::-1]) for x in lst])), primes_up_to(max([int(str(x)[::-1]) for x in lst])))]
    emirps = set(
        [x if ((x in lst) and (int(str(x)[::-1]) in lst) and str(x)[::-1] != str(x)) else None for x in range(n + 1)])
    emirps.remove(None)
    return [len(emirps), max(emirps), sum(emirps)]


print(find_emirp(50))
