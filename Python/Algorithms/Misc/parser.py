
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Parser:
    def __init__(self, parser, char=None,) -> None:
        if char == None:
            self.parser = parser
            self.char = None
        else:
            self.parser = lambda string: parser(string,char)
            self.char = char
        self.index = 0
        self.result = ('','')
        self.err = ''
        self.is_err = False

    def __lshift__(self, parser):
        ...

    def __rshift__(self, parser):
        def closure(string):
            s1,s2 = self(string)
            s3,s2 = parser(s2)
            return s1+s3, s2
        return Parser(closure)

    def __or__(self, parser):
        def closure(string):
            try: s1,s2 = self(string)
            except StopIteration: s1,s2 = parser(string)
            return s1, s2
        return Parser(closure)

    def __call__(self, string):
        return self.parser(string)


'''-----------------Parser Functions----------------------------------------'''

def parse_char(string, char, idx=0,end=False):
    if not string:
        if end == False:
            raise ValueError(f"Nothing to Parse")
    
    if string[idx] == char:
        return char, string[idx+1:]
    
    else:
        raise StopIteration(f'Expected "{char}", found "{string[idx]}"')

def ignore_until_char(string, char, idx=0):
    if not string:
        raise ValueError(f"Nothing to Parse")
    while 1:
        try:
            s1,s2 = parse_char(string[idx:],char)
            return string[:idx] + s1, s2
        except StopIteration:
            idx += 1
            continue
        except ValueError:
            raise ValueError(f'{char} not found in {string}')

def parse_end(string, idx=0):
    if not string:
        return '',''
    else:
        raise ValueError('Not End of Input')


'''------------------------Parser Generators--------------------------------'''

from functools import reduce
import operator

def match(string):
    if not string:
        raise ValueError
    # parser = reduce(lambda b,i: Parser(parse_char,string[i])>>b,range(len(string)),Parser(parse_char,string[0]))
    if string[0] == '^':
        string = string[1:]
        parser = Parser(parse_char,string[0])
    else:
        parser = Parser(ignore_until_char,string[0])
    if string[-1] == '$':
        string = string[:-1]
        for idx in range(1,len(string)):
            parser >>= Parser(parse_char, string[idx])
        parser >>= Parser(parse_end)
    else:
        for idx in range(1,len(string)):
            parser >>= Parser(parse_char, string[idx])
    return parser

# print(ignore_until_char('ancxqeiuzasda','z'))

A = Parser(parse_char, 'a')
B = Parser(parse_char, 'b')
C = Parser(parse_char, 'c')
AB = A>>B
AoB = A|B
print(parse_char('abc','a'))
print(A('abc'))
print(B('bac'))
print(AB('abc'))
print(AoB('abc'))
print(AoB('bac'))
ABC = A>>B>>C
AoBoC = A|B|C
print(ABC('abc'))
print(AoBoC('abc'))
print(AoBoC('bac'))
print(AoBoC('cab'))
AoBoCBC = (A|B|C)>>(B>>C)
print(AoBoCBC('abc'))

MatchABC = match('abc')

print(MatchABC('xzkjuuoxuzcbabcsdiiyfasffa'))

MatchABC = match('^abc')

print(MatchABC('abcsdiiyfasffa'))

MatchABC = match('abc$')

print(MatchABC('xzkjuuoxuzcbabc'))

MatchABC = match('^abc$')

print(MatchABC('abc'))


