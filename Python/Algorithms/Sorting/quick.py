'''

Algorithm Name plus Description


How many approaches?

'''

from random import randint

# Approach 1

def quick(sequence):
    if len(sequence) <= 1: return sequence
    pivot = sequence[randint(0,len(sequence)-1)]
    lt =[]
    gt = []
    for i in sequence:
        if i > pivot:
            gt.append(i)
        elif i < pivot:
            lt.append(i)
    return quick(lt) + [pivot] + quick(gt)

# Approach 2



# Testing

def main():
    print(quick([0,2,1]))
    print(quick([0,1,2,3,4,5]))
    print(quick([5,4,3,2,1,0]))
    print(quick([0,5,3,2,4,1]))
    print(quick([3,76,1,30,29]))

if __name__ == '__main__':
    main()
