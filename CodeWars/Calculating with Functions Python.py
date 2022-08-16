def zero(*a): return 0 if len(a) == 0 else eval(rf'0{a[0]}')


def one(*a): return 1 if len(a) == 0 else eval(rf'1{a[0]}')


def two(*a): return 2 if len(a) == 0 else eval(rf'2{a[0]}')


def three(*a): return 3 if len(a) == 0 else eval(rf'3{a[0]}')


def four(*a): return 4 if len(a) == 0 else eval(rf'4{a[0]}')


def five(*a): return 5 if len(a) == 0 else eval(rf'5{a[0]}')


def six(*a): return 6 if len(a) == 0 else eval(rf'6{a[0]}')


def seven(*a): return 7 if len(a) == 0 else eval(rf'7{a[0]}')


def eight(*a): return 8 if len(a) == 0 else eval(rf'8{a[0]}')


def nine(*a): return 9 if len(a) == 0 else eval(rf'9{a[0]}')


def plus(a): return rf'+{a}'


def minus(a): return rf'-{a}'


def times(a): return rf'*{a}'


def divided_by(a): return rf'//{a}'


print(seven(times(five())))
