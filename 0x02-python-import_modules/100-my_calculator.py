#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys

    n_argv = len(sys.argv)
    argv = sys.argv

    if (n_argv != 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = argv[1]
        b = argv[3]
        op = argv[2]

        if (op == "+"):
            print('{:s} + {:s} = {:d}'.format(a, b, add(int(a), int(b))))
        elif (op == "-"):
            print('{:s} - {:s} = {:d}'.format(a, b, sub(int(a), int(b))))
        elif (op == "*"):
            print('{:s} * {:s} = {:d}'.format(a, b, mul(int(a), int(b))))
        elif (op == "/"):
            print('{:s} / {:s} = {:d}'.format(a, b, div(int(a), int(b))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
