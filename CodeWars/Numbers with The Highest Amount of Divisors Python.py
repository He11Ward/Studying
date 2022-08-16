def valid_ISBN10(isbn):
    return len(isbn) == 10 and sum(
        [(i + 1) * j for i, j in enumerate(
            [int(j) if j.isnumeric() else (10 if i == 9 and j == "X" else 0.01) for i, j in
             enumerate(isbn)])]) % 11 == 0


print(valid_ISBN10('1293'))
print(valid_ISBN10('1112223339'))
print(valid_ISBN10('048665088X'))
print(valid_ISBN10('ABCDEFGHIJ'))
print(valid_ISBN10('22088078631'))
print(valid_ISBN10('123456789T'))
