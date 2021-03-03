
'''--------------------------------------------Modified-----------------------------------------------------'''

def parse_char(string):
    if not string:
        raise StopIteration
    else:
        return string[0], string[1:]

def parse_until(string, *char):
    chars = set(char)
    parsed = ''
    sep = ''
    s1,s2 = '', string
    try:
        while 1:
            s1, s2 = parse_char(s2)
            if s1 in chars:
                sep = s1
                raise StopIteration
            parsed += s1
    except StopIteration:
        return parsed, sep, s2

def parse_int(string,start='',sep='\t'):
    return f'Integer(\n{start}{sep}{sep}{string}\n{start}{sep})'

def parse_float(string,start='',sep='\t'):
    return f'Float(\n{start}{sep}{sep}{string}\n{start}{sep})'

def parse_number(string,start='',sepr='\t'):
    parsed = ''
    s1,s2 = '',string
    try:
        if not string: return string
        s1,sep,s2 = parse_until(s2,'.')
        if not s2:
            s1 = parse_int(s1,start,sepr)
        else:
            s1 = parse_float(s1+sep+s2,start,sepr)
        parsed += s1
        raise StopIteration
    except StopIteration:
        return parsed


def parse_bool(string,start='',sep='\t'):
    if string == 'true' or string == 'false':
        return f'Boolean(\n{start}{sep}{sep}{string}\n{start}{sep})'
    else: return string

def parse_list(string,start='',sepr='\t'):
    parsed = ''
    s1,s2 = '',string
    try:
        s1, s2 = parse_char(s2)
        if s1 != '[': raise StopIteration
        else: parsed += f'{start}List(\n{start}'
        while 1:
            s1,s2 = parse_char(s2)
            if s1 in types:
                s1,s2 = types[s1[0]](s1+s2,sepr,sepr)
                parsed += s1
                continue
            else: s2 = s1 + s2
            s1, sep, s2 = parse_until(s2, ',',']')
            if s1 in bools: s1 = parse_bool(s1,start,sepr)
            else: s1 = parse_number(s1,start,sepr)
            if sep == ']':
                parsed += sepr + s1
                raise StopIteration
            parsed += sepr + s1 + f',\n{start}'
    except StopIteration:
        return parsed + f'\n{start})', s2

def parse_string(string,start='',sepr='\t'):
    parsed = ''
    s1,s2 = '',string
    try:
        s1, s2 = parse_char(s2)
        if s1 != '"': raise StopIteration
        else: parsed += f'{start}List(\n{start}'
        while 1:
            s1,s2 = parse_char(s2)
            if s1 in types:
                s1,s2 = types[s1[0]](s1+s2,sepr,sepr)
                parsed += s1
                continue
            else: s2 = s1 + s2
            s1, sep, s2 = parse_until(s2, ',',']')
            if s1 in bools: s1 = parse_bool(s1,start,sepr)
            else: s1 = parse_number(s1,start,sepr)
            if sep == '"':
                parsed += sepr + s1
                raise StopIteration
            parsed += sepr + s1 + f',\n{start}'
    except StopIteration:
        return parsed + f'\n{start})', s2

'''-----------------------------------------Original--------------------------------------------------------'''
'''
def parse_until(string, *char):
    chars = set(char)
    parsed = ''
    sep = ''
    s1,s2 = '', string
    try:
        while 1:
            s1, s2 = parse_char(s2)
            if s1 in chars:
                sep = s1
                raise StopIteration
            parsed += s1
    except StopIteration:
        return parsed, sep, s2

def parse_int(string,start='',sep='\t'):
    return f'Integer(\n{string}\n)'

def parse_float(string,start='',sep='\t'):
    return f'Float(\n{string}\n)'

def parse_number(string,start='',sep='\t'):
    parsed = ''
    s1,s2 = '',string
    try:
        if not string: return string
        s1,sep,s2 = parse_until(s2,'.')
        if not s2:
            s1 = parse_int(s1,)
        else:
            s1 = parse_float(s1+sep+s2,)
        parsed += s1
        raise StopIteration
    except StopIteration:
        return parsed


def parse_bool(string,start='',sep='\t'):
    if string == 'true' or string == 'false':
        return f'Boolean(\n{string}\n)'
    else: return string

def parse_list(string,start='',sep='\t'):
    parsed = ''
    s1,s2 = '',string
    try:
        s1, s2 = parse_char(s2)
        # s1, s2 = parse_char(s2)
        if s1 != '[': raise StopIteration
        else: parsed += 'List(\n'
        while 1:
            s1,s2 = parse_char(s2)
            print(s1,s2)
            print()
            if s1 in types:
                s1,s2 = types[s1[0]](s1+s2,)
                parsed += s1
                print(parsed)
                print()
                continue
            else: s2 = s1 + s2
            s1, sep, s2 = parse_until(s2, ',',']')
            print(s1,sep,s2)
            print()
            if s1 in bools: s1 = parse_bool(s1,)
            else: s1 = parse_number(s1,)
            if sep == ']':
                parsed += s1
                raise StopIteration
            parsed += s1 + f',\n'
            print(parsed)
            print()
    except StopIteration:
        return parsed + f'\n)', s2

'''

bools = {
    'true',
    'false'
}

types = {
    '[': parse_list,
    # '{': Dict
    # "\"": String,
}


def main(argv):
    # string = '[0,1.2,true,[1,false,3],5]'
    string = argv[1]
    print(string)
    print(parse_list(string))

# 

import sys
if __name__ == '__main__':
    main(sys.argv)