class Success:
    def __init__(self, success) -> None:
        self.success = success

    def unwrap(self):
        return self.success

    def __repr__(self) -> str:
        return f'Success: {self.success}'

class Failure:
    def __init__(self, failure) -> None:
        self.failure = failure

    def unwrap(self):
        return self.failure

    def __repr__(self) -> str:
        return f'Failure: {self.failure}'

class Result:

    def __init__(self, success=None, failure=None) -> None:
        self.result = Success(success) if not failure else Failure(failure)
    
    def unwrap(self):
        return self.result.unwrap()

    def get(self):
        return self.result

    def __repr__(self) -> str:
        return f'{self.result}'

def pchar(char: str):
    def parser(input: str) -> Result:
        if input == '':
            return Result(failure="No more input")
        else:
            if input[0] == char:
                return Result(success=(char, input[1:]))
            else:
                return Result(failure=f"Expecting '{char}'': Got '{input[0]}'")
    return parser

def run(parser, input: str) -> Result:
    return parser(input)

class Parser:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)

    def __rshift__(self, parser):
        def closure(input: str) -> Result:
            result1 = run(self, input)
            if isinstance(result1.get(), Failure):
                return result1
            else:
                value1, remaining1 = result1.unwrap()
                result2 = run(parser, remaining1)
                if isinstance(result2.get(), Failure):
                    return result2
                else:
                    value2, remaining2 = result2.unwrap()
                combined_value = value1, value2
                return Result(success=(combined_value, remaining2))
        return Parser(closure)

    def __lshift__(self, func):
        '''
            This is also known as the map
        '''
        def closure(input: str) -> Result:
            result = run(self, input)
            if isinstance(result.get(), Success):
                return func(result.unwrap())
            else:
                return result
        return Parser(closure)

    def __or__(self, parser):
        '''
            This is our parser's orElse function which will map one function to another
        '''
        def closure(input: str) -> Result:
            result1 = run(self, input)
            if isinstance(result1.get(), Success):
                return result1
            else:
                result2 = run(parser, input)
                return result2
        return Parser(closure)

def and_then(parser1, parser2) -> Result:
    def closure(input: str) -> Result:
        result1 = run(parser1, input)
        if isinstance(result1.get(), Failure):
            return result1
        else:
            value1, remaining1 = result1.unwrap()
            result2 = run(parser2, remaining1)
            if isinstance(result2.get(), Failure):
                return result2
            else:
                value2, remaining2 = result2.unwrap()
            combined_value = value1, value2
            return Result(success=(combined_value, remaining2))
    return closure

def or_else(parser1, parser2) -> Result:
    def closure(input: str) -> Result:
        result1 = run(parser1, input)
        if isinstance(result1.get(), Success):
            return result1
        else:
            result2 = run(parser2, input)
            return result2
    return closure

def parser_map(parser, func) -> Result:
    def closure(input: str) -> Result:
        result = run(parser, input)
        if isinstance(result.get(), Success):
            return func(result.unwrap())
        else:
            return result
    return closure



parse_letter

parse_a = Parser(pchar('a'))
parse_b = Parser(pchar('b'))
parse_o = Parser(pchar('o'))
parse_z = Parser(pchar('z'))

parse_ab = parse_a >> parse_b
parse_oz = parse_o >> parse_z
parse_aboz = parse_ab | parse_oz

parse-plus

print(
    parse_aboz('aboz'),
    parse_ab('aboz'),
    parse_aboz('ab'),
    parse_aboz('oz'),
    sep='\n'
)
