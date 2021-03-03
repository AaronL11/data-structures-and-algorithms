'''

    Helper function that checks if a given sequence is sorted

'''


def is_sorted(sequence):
    x = 0
    seq = iter(sequence)
    is_sorted = True
    while is_sorted:
        try:
            i = next(seq)
            if x <= i:
                x = i
                continue
            else:
                is_sorted = False
        except StopIteration:
            break
    return is_sorted