import sys

def fizzbuzz(num, fizz, buzz):
    '''
    INPUT: int, int, int
    OUTPUT: string

    Return "Fizz" if num is divisible by fizz,
           "Buzz" if num is divisible by buzz,
           "FizzBuzz" if num is dibisible by both fizz and buzz, and
           "" otherwise
    '''
    pass



if __name__ == '__main__':
    print fizzbuzz(int(sys.argv[1]), 3, 5)
