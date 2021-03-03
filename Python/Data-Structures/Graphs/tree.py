'''

    Tree
    
    We are doing a simple Class based approach
    
    The Tree class simply holds 

'''

# Approach 1

# Useful typing module

from typing import Any, Iterable

class DFSIter:
    def __init__(self, tree) -> None:
        self._tree = [DFSIter(leaf) for leaf in tree] if tree.get_branch() != None else None
        self._terminal = True if self._tree == None else False
        self._n = 0
        self._max = len(self._tree) if self._tree != None else 0
    
    def __next__(self):
        if self._n >= self._max:
            raise StopIteration
        else:
            self._n += 1
            ...

            return next(self._tree[self._n])


class Node:
    '''
        Hello
    '''
    def __init__(self, name: Any, branches=None) -> None:
        self._name = name
        self._terminal = branches == None
        self._branches = [Node(leaf) for leaf in branches] if not self._terminal else None
    
    def add_branch(self, branches: Iterable) -> None:
        self._branches = [Node(leaf) for leaf in branches] if self._terminal else self._branches + [Node(leaf) for leaf in branches]

    def get_name(self) -> Any:
        return self._name

    def get_branch(self) -> Any:
        return self._branches

    def find_dfs(self, name) -> tuple:
        stack = []
        if not self._terminal:
            for leaf in self._branches:
                if name == leaf.get_name():
                    return True, stack + [name]
                else:
                    stack.append(leaf.get_name())
                    flag, stx = leaf.find_dfs(name)
                    if flag:
                        return True, stack + stx
                    else:
                        del stx
                        stack.pop()
            return False, stack
        else: return False, stack

    def find_bfs(self, name) -> tuple:
        stack = [self._name]
        queue = []
        if not self._terminal:
            queue = self._branches
            for leaf in queue:
                if name == leaf.get_name():
                    return True, queue, stack + [name]
            return False, queue, stack
        else: return False, queue, stack

    def __eq__(self, thing) -> bool:
        return self._name == thing

    def __req__(self, thing) -> bool:
        return self._name == thing

    def __lt__(self, thing) -> bool:
        return self._name < thing

    def __rlt__(self, thing) -> bool:
        return self._name < thing

    def iter_dfs(self):
        self._idx = 0
        return (leaf.iter_dfs() for leaf in self._branches)
        return iter(self._branches)

    def next_dfs(self):
        if self._idx >= len(self._branches):
            raise StopIteration
        else:

            if not self._terminal:
                result = self._branches[self._idx]
                self._idx += 1
                return result

    def __iter__(self):
        return iter(self._branches)

    def __getitem__(self, name):
        return self._branches[self._branches.index(name)]

    '''----------------------------------------------------------------'''

    def __repr__(self) -> str:
        return f"Node({self._name})" if self._branches == None else f"Node({self._name}, [{', '.join(repr(leaf) for leaf in self._branches)}])"
    
    def __str__(self) -> str:
        return f"{self._name}" if self._branches == None else f"{self._name}: [{', '.join(f'{leaf}' for leaf in self._branches)}]"

'''

Now begins the Tree Class

'''

class Tree:
    '''
        This class is responsible for storing our values and is ultimately what the end-user will interact with.
        The data is stored in a dictionary with the key being the name that was passed in.
        
        Printing has been implemented as well as a few operations. Mainly equality operations for use in Binary Search Trees.
    '''
    def __init__(self, root: Any, branches: Iterable, **kwargs) -> None:
        self._root = root
        self._branches = {leaf: Node(leaf) for leaf in branches}

    def add_branch(self, name: Any, branches: Iterable) -> None:
        if name in self._branches:
            self._branches[name].add_branch(branches)
        else:
            stack = self.find_dfs(name)
            stack.remove(self._root)
            if stack != []:
                l = self._branches
                for i in stack:
                    l = l[i]
                l.add_branch(branches)


    def get_root(self) -> Any:
        return self._root

    def get_branch(self, name) -> Any:
        return self._branches.get(name)

    def find_dfs(self, name) -> list:
        stack = [self._root]
        for leaf in self._branches.values():
            if name == leaf.get_name():
                return stack + [name]
            else:
                stack.append(leaf.get_name())
                flag, stx = leaf.find_dfs(name)
                if flag:
                    return stack + stx
                else:
                    del stx
                    stack.pop()
        return []

    def find_bfs(self, name) -> list:
        queue = list(self._branches.values())
        stack = [self._root]
        idx = 0
        while idx < len(queue):
            flag, new, stx = queue[idx].find_bfs(name)
            if not flag:
                del stx
                queue += new
                del new
            else:
                del new
                return stack + stx
            idx += 1
        return [] 

    def __iter__(self):
        return iter(self._branches.values())

    def iter_dfs(self):
        return DFSIter(self)

    def __repr__(self) -> str:
        return f"Tree({self._root}, [{', '.join(repr(leaf) for leaf in self._branches.values())}])"

    def __str__(self) -> str:
        return f"{self._root}: [{', '.join(f'{leaf}' for leaf in self._branches.values())}]"

# Approach 2

# Testing
def main():
    tree = Tree('a', ['b','c','d'])
    tree.add_branch('b', [1,2,3])
    tree.add_branch('c', [4,5,6])
    tree.add_branch('d', [7,8,9])
    # print(str(tree))
    # print(repr(tree))

    # Binary Search Tree
    bst = Tree(50, [25, 75])
    bst.add_branch(25, [13, 38])
    bst.add_branch(75, [63, 88])
    low = bst
    # while (low := max(low)).get_branch():
    #     ...
    # print(low)
    # x = bst.find_dfs(88)
    print(bst.find_dfs(88))
    print(tree.find_dfs(9))
    print(bst.find_bfs(88))
    print(tree.find_bfs(9))
    # print(r := min(min(bst)))
    # print(min(r))

    bst.add_branch(13, [6, 18])
    print(bst)
    # print(bst.find_bfs(6))
    bst.add_branch(6, [3, 9])
    bst.add_branch(88, [82, 94])
    bst.add_branch(38, [32, 44])
    print(bst)

    ...

if __name__ == '__main__':
    main()