#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as Er:
        print("Exception: {}".format(Er), file=sys.stderr)
        return None
