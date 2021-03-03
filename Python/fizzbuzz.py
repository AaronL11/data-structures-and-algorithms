# FizzBuzz
# 
# If the number is divisible by 3 print Fizz,
# If the number is divisble by 5 print Buzz,
# If the number is divisble by 15 print FizzBuzz,
# 
# 

'''
    Ultimately we're basically looping through a sequence and just matching the 
    appropriate word to the letter:
    [  3,       5,]
    ['Fizz', 'Buzz',]

    So for this solution I simply wrote a function that creates a generator that will loop through the given range.

    We can 

    We use closures to capture the initial datum, and we simply put we return a generator or value, depending on what we pass in.
'''

def fizz_buzz(**fb):
    # evaluates the fizzbuzz, based on the given parameters
    def eval(i):
        return s if (s:=''.join(s for s,n in fb.items() if i%n==0)) else i
    # generator for getting all fizzbuzz through a range
    def gen(stop,start=0):
            i = start
            while i<=stop:
                yield eval(i)
                i += 1
    # the closure that handles our logic
    def closure(range=None, at=0):
        return gen(range,start=at) if range else eval(at)
    
    return closure

def main():
    # get the 99th num
    print(fizz_buzz(Zip=2,Fizz=3,Buzz=5,Zap=10)(at=99))
    # loop through all values from 0-100
    for i in fizz_buzz(Zip=2,Fizz=3,Buzz=5,Zap=10)(range=100):
        print(i)
    # last 50 values
    for i in fizz_buzz(Zip=2,Fizz=3,Buzz=5,Zap=7,Zop=11)(range=100,at=50):
        print(i)

if __name__ == '__main__':
    main()
