def is_substring(s1, s2):
    return s2 in s1

def is_rotation(s1, s2):
    if len(s1) == len(s2):
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    else:
        return False