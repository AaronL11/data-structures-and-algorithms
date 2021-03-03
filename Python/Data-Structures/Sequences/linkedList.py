
from typing import Container


class Link:

    def __init__(self, name=None, link=[]) -> None:

        self._name = name
        if link==[]:
            self._link = None
            self._terminal = True
        else:
            self._link = Link(link[0], link[1:])
            self._terminal = False

    def get_name(self):
        return self._name

    def set_link(self, link):
        self._link = link if isinstance(link, Link) else Link(link)

    def __iter__(self):
        return LinkIter(self)

    def is_end(self):
        return self._terminal


    def __next__(self):
        if self._terminal or self._link == None:
            raise StopIteration
        else:
            return self._link

    def __repr__(self) -> str:
        return f"Link({self._name}, {repr(self._link)})"

    def __str__(self) -> str:
        return f'{self._name}'

class LinkIter:

    def __init__(self, link) -> None:
        self._chain = link
        self._first = True
    
    def __next__(self):
        if self._chain.is_end():
            raise StopIteration
        else:
            if self._first:
                self._first = False
                return self._chain._name
            self._chain = next(self._chain)
            return self._chain

class LinkedList:

    @staticmethod
    def of(*args):
        return LinkedList(args[0], list(args[1:]))

    def __init__(self, name=None, link=[]) -> None:

        self._name = name
        # self._name = Link(name, link)
        if link==[]:
            self._link = None
            self._terminal = True
        else:
            self._link = Link(link[0], link[1:])
            self._terminal = False

    def get_name(self):
        return self._name

    def __iter__(self):
        return LinkIter(self)

    def is_end(self):
        return self._terminal

    def add(self, element):
        x = 0
        for i in self._link:
            x = i
        x.set_link(element)

    def delete(self, element):
        last = self
        delete = False
        for i in self._link:
            if i==element:
                delete = True
                continue
            if delete:
                last.set_link(i)
                break
            else:
                last = i

    def __next__(self):
        if self._terminal or self._link == None:
            raise StopIteration
        else:
            return self._link

    def __repr__(self) -> str:
        return f"Link({self._name}, {repr(self._link)})"

    def __str__(self) -> str:
        return f'{self._name}'


def main():
    ll = LinkedList.of(0,1,2,3,4,5)
    print(ll)
    print(repr(ll))
    for i in ll:
        print(repr(i))


if __name__ =='__main__':
    main()