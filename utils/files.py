def delete_linebreak(s):
    if '\n' in s:
        return s[:len(s) - 1]
    else:
        return s
