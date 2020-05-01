#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_argv = len(argv)
    sum = 0

    for i in range(1, n_argv):
        sum += int(argv[i])

    print('{}'.format(sum))
