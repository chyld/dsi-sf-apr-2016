import ipdb

def hello_world():
    s = 'hello, gaia!'
    print('***> s: {0}'.format(s))

def add_em_up(a, b, c):
    return a + b + c

if __name__ == '__main__':
    hello_world()
    total = add_em_up(2, 3, 4)
    ipdb.set_trace()
    print('***> total: {0}'.format(total))

# ipython:
# import hello as h
# h.hello_world()

# python hello.py
# ipython hello.py
