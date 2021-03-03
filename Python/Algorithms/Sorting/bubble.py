'''

Algorithm Name plus Description


How many approaches?

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

# Approach 1

def bubble(sequence):
    isort = False
    while not isort:
        isort = True
        x = 0
        i = -1
        for j,n in enumerate(sequence):
            if x > n:
                sequence[i], sequence[j] = sequence[j], sequence[i]
                isort = False
            x = n
            i += 1
    return sequence

# Approach 2



# Testing

def main():
    print(bubble([5,6,3,0,1,39,4,14]))
    print(is_sorted([3,6,8,10]))

if __name__ == '__main__':
    main()
