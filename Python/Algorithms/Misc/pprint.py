'''

This is a recursive attempt I had at pretty printing.


How many approaches?

'''

# Approach 1

def pprint(sequence,sep='\t',start=''):
    def pprintlist(sequence, start=start,sep=sep):
        if isinstance(sequence[0], list):
            string = f'{start}[\n' + pprinter(sequence[0],start=f'{start}{sep}',sep=sep)
        else:
            string = f'{start}[\n{start}{sep}' + str(sequence[0])
        for element in sequence[1:]:
            if isinstance(element, list):
                string += f',\n' + pprinter(element,start=f'{start}{sep}',sep=sep)
            else:
                string += f',\n{start}{sep}' + str(element)
        return string + f'\n{start}]'
    print(pprintlist(sequence))


def pprinter(sequence, start='',sep='\t'):
    if isinstance(sequence[0], list):
        string = f'{start}[\n' + pprinter(sequence[0],start=f'{start}{sep}',sep=sep)
    else:
        string = f'{start}[\n{start}{sep}' + str(sequence[0])
    for element in sequence[1:]:
        if isinstance(element, list):
            string += f',\n' + pprinter(element,start=f'{start}{sep}',sep=sep)
        else:
            string += f',\n{start}{sep}' + str(element)
    return string + f'\n{start}]'


# Approach 2

pprint(
    [
        [0,1,2,3,4],
        [0,1,2,3,4],
        [0,1,2,3,4],
        [0,1,2,3,4]
    ]
)

# Testing

def main():
    # x = [1,2,3,4,5]
    # print(pprinter(x,sep='-'))
    # y = [[1,2,3],[4,5,6],[6,7,8]]
    # print(pprinter(y,sep='-'))
    z = [[[1,2,3],[4,5,6],[7,8,9]],[['a','b','c'],['d','e','f'],['g','h','i']]]
    print(pprinter(z))
    # for i in x:
    #     pprint(i)

if __name__ == '__main__':
    main()
