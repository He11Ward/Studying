def valid_ISBN10(isbn):
    return len(isbn) == 10 and sum(
        [(i + 1) * j for i, j in enumerate(
            [int(j) if j.isnumeric() else (10 if i == 9 and j == "X" else 0.01) for i, j in
             enumerate(isbn)])]) % 11 == 0
