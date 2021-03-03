
'''

Algorithm Name plus Description


How many approaches?

'''

# Approach 1

def insertion(sequence):
    slist = [sequence[0]]
    for i in sequence:
        for j,y in enumerate(slist):
            if y > i:
                slist.insert(j,i)
                break
            elif j == len(slist)-1 and y!=i:
                slist.append(i)
                break
    return slist

# Approach 2



# Testing

def main():
    print(insertion([0,1,2,3,4,5]))
    print(insertion([5,4,3,2,1,0]))
    print(insertion([4,5,2,3,0,1]))

if __name__ == '__main__':
    main()
