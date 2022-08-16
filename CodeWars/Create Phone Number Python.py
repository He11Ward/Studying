def create_phone_number(n):
    return ''.join(['(', ''.join([str(s) for s in n[:3]]), ') ', ''.join([str(s) for s in n[3:6]]), '-', ''.join([str(s) for s in n[6:10]])])