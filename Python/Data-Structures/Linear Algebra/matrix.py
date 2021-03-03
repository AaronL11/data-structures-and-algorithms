'''

    Data Structure Name Plus Description
    
    Implementation Approaches and Details

'''

# Approach 1

from typing import Any

class Matrix:

    '''-----------------------------------------------------------------------------------------'''

    @staticmethod
    def id(row: int, column: int) -> Any:
        return Matrix([[1 if i==j else 0 for j in range(column)] for i in range(row)])

    '''-----------------------------------------------------------------------------------------'''

    def __init__(self, array2d) -> None:
        self._mat = array2d
        self._rows = len(array2d)
        self._cols = len(array2d[0])

    @property
    def T(self):
        return Matrix([[row[i] for row in self._mat] for i in range(self._cols)])

    @property
    def flatten(self):
        return

    @property
    def cof(self):
        return

    def minor(self, row, column):
        
        return

    @property
    def inv(self):
        return

    @property
    def det(self):
        return 


    @property
    def REF(self):
        ref = [[j for j in i] for i in self]
        rows,cols = self._rows,self._cols
        l = 0
        while l<rows:
            pivot = ref[l][l]
                
            for i in range(l+1,rows):
                ref[i] = subtract(scale(pivot, ref[i]), scale(ref[i][l], ref[l]))
            l+=1

        return Matrix(ref)

    @property
    def RREF(self):
        rref = [[j for j in i] for i in self]
        rows,cols = self._rows,self._cols
        l = 0
        while l<rows:
            pivot = rref[l][l]
                
            for i in range(l+1,rows):
                rref[i] = subtract(scale(pivot, rref[i]), scale(rref[i][l], rref[l]))
            l+=1
        l-=1
        while l>-1:
            num = rref[l][l]
            rref[l] = scale(1/num,rref[l])
            for i in range(l-1,-1, -1):
                rref[i] = subtract(rref[i],scale(rref[i][l],rref[l]))
            l-=1
        return Matrix(rref)

    '''-----------------------------------------------------------------------------------------'''

    def columns(self):
            return ((row[i] for row in self._mat) for i in range(self._cols))

    def transpose(self) -> Any:
        return Matrix([[row[i] for row in self._mat] for i in range(self._cols)])

    '''------------------------------------------------------------------------------------------'''

    def __repr__(self) -> str:
        x = ',\n\t'
        y = ','
        return f"Matrix(\n\t{x.join(f'[{y.join(str(e) for e in row)}]' for row in self._mat)}\n)"

    def __str__(self) -> str:
        x = '\n'
        y = ','
        return f"{x.join(f'[{y.join(str(e) for e in row)}]' for row in self._mat)}"

    '''------------------------------------------------------------------------------------------'''

    def __neg__(self):
        return -1*self

    def __add__(self, mat):
        return Matrix([[a+b for a,b in zip(x,y)] for x,y in zip(self,mat) ])

    def __sub__(self, mat):
        return self + -mat

    def __matmul__(self, mat):
        return Matrix([[sum(a*b for a,b in zip(r,c)) for c in mat.columns()] for r in self])

    def __rmatmul__(self,mat):
        return Matrix([[sum(a*b for a,b in zip(r,c)) for c in self.columns()] for r in mat])

    def __call__(self, v):
        return [sum(a*b for a,b in zip(r,v)) for r in self]

    '''------------------------------------------------------------------------------------------'''

    def __mul__(self, num: int):
        return Matrix([[num*a for a in row] for row in self])

    def __rmul__(self, num: int):
        return Matrix([[num*a for a in row] for row in self])

    def __truediv__(self,num):
        return Matrix([[a/num for a in row] for row in self])

    def __floordiv__(self,num):
        return Matrix([[a//num for a in row] for row in self])

    def __mod__(self, num):
        return Matrix([[a%num for a in row] for row in self])

    '''------------------------------------------------------------------------------------------'''

    def __iter__(self):
        return iter(self._mat)

    def __getitem__(self, indexes):
        i,j = indexes
        return self._mat[i-1][j-1]

    def __setitem__(self, indexes, newitem):
        i,j = indexes
        self._mat[i-1][j-1] = newitem


''' ------------------------Helper Functions------------------------------- '''

def det(A):
    return A.det

def scale(n, row):
    return [n*r for r in row]

def subtract(row1,row2):
    return [a-b for a,b in zip(row1,row2)]

# Approach 2

# Testing
def main():
    hmm = Matrix([
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4]
    ])
    print(hmm)
    print(repr(hmm))
    print(hmm.T)
    print()
    id_four = Matrix.id(4,4)
    print(id_four)
    print()
    print(hmm + hmm.T)
    print()
    print(hmm - hmm.T)
    print()
    print(hmm*2)
    print()
    print(hmm/2)
    print()
    print(hmm//2)
    print()
    print(hmm%2)
    print()
    print(hmm[(1,2)])
    print()
    print(hmm @ hmm.T)
    print()
    print(hmm @ id_four)
    print()
    print(hmm([1,2,3,4]))
    print()
    hmm2 = Matrix([
        [1,2,3,4],
        [5,6,7,8],
        [9,8,3,2],
        [4,6,9,4],
    ])
    print(hmm2)
    print()
    print(hmm2.REF)
    print()
    print(hmm2.RREF)
    print()

if __name__ == '__main__':
    main()
