#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}\n".format(value))
        return True

    except Exception as Er:
        sys.stderr.write("Exception: {}".format(Er.args[0]))
        return False
