'''

Algorithm Name plus Description


How many approaches?

'''

# Approach 1

def ref(matrix):
    rows = len(matrix[0])
    l = 0
    while l<rows:
        pivot = matrix[l][l]
        for i in range(l+1,rows):
            n = matrix[i][l]
            matrix[i] = [a-b for a,b in zip([pivot*i for i in matrix[i]],[n*i for i in matrix[l]])]
            # matrix[i] = subtract(scale(pivot, matrix[i]), scale(matrix[i][l], matrix[l]))
        l+=1
    return matrix

# Approach 2


# Utility Functions

def scale(n, row):
    return [n*i for i in row]

def subtract(row1, row2):
    return [a-b for a,b in zip(row1,row2)]

# Testing

def main():
    

if __name__ == '__main__':
    main()
