#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_argv = len(argv)

    if (n_argv == 1):
        print('0 arguments.')
    elif (n_argv == 2):
        print('1 argument:')
        print('1: {:s}'.format(argv[1]))
    else:
        print('{:d} arguments:'.format(n_argv - 1))
        for i in range(1, n_argv):
            print('{:d}: {:s}'.format(i, argv[i]))
