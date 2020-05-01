#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list = dir(hidden_4)

    for line in list:
        if line[0] != "_":
            print("{}".format(line))
