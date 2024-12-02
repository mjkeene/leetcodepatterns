def one_away(s1, s2):
    """
    pale, ple -> True
    pales, pale -> True
    pale, bae -> False
    apple, aple -> True
    """
    if abs(len(s1) - len(s2)) > 1:
        return False

    # edit, insert, or remove
    # insert and remove are inverses of each other, i.e., apple to aple, you can either
    # remove one p from apple or add one p to aple
    s1_arr, s2_arr = list(s1), list(s2)
    str_len = min(len(s1), len(s2))
    difference_seen = False

    # if there is a diff seen, shift longer string index by 1
    for i in range(str_len):
        if s1_arr[i] != s2_arr[i] and not difference_seen:
            difference_seen = True
            if len(s1) > len(s2):
                del s1_arr[i]
            elif len(s2) > len(s1):
                del s2_arr[i]
        elif s1_arr[i] != s2_arr[i] and difference_seen:
            return False

    return True
