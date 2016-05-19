def hello_world():
    s = 'hello, gaia!'
    print('***> s: {0}'.format(s))

def add_em_up(a, b, c):
    return a + b + c

if __name__ == '__main__':
    hello_world()
    print('***> add_em_up(2,3,4): {0}'.format(add_em_up(2,3,4)))

# ipython
# import hello as lib
# lib.hello_world()
