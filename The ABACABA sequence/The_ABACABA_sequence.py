def acab_sequence(n):
    return "" if n == 0 else (prev:=acab_sequence(n-1)) + chr(96+n) + prev