def solution(s):
    return [s[x:x + 2] if len(s[x:x + 2]) == 2 else s[x:x + 2] + '_' for x in range(0, len(s), 2)]
