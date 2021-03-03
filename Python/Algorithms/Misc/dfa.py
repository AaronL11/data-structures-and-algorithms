
def grab(string):
    return (string, '') if len(string) == 0 else (string[0], string[1:])

def parse(string):
    return stateA(string)

def stateA(string):
    s1, s2 = grab(string)
    return stateB(s2)

def stateB(string):
    s1, s2 = grab(string)
    return stateC(s2)

def stateC(string):
    s1, s2 = grab(string)
    return stateD(s2) if len(s1) > 0 else True

def stateD(string):
    if not string: return False
    s1, s2 = grab(string)
    return stateD(s2)

def main(argv):
    string = argv[1]
    # print(grab(string))
    print(parse(argv[1]))

import sys
if __name__ == '__main__':
    main(sys.argv)