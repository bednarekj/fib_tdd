def fib_nums():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


def find_term(digit_limit):
    for term_nr, fib in enumerate(fib_nums(), start=1):
        if digit_limit <= len(str(fib)):
            return 'F{0}'.format(term_nr)


if __name__ == '__main__':
    print(find_term(1000))