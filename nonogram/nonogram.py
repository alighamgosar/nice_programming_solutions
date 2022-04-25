def nonogram(row):
    s = ''.join(map(str, row))
    result = [len(x) for x in s.split('0') if len(x) > 0]
    return result