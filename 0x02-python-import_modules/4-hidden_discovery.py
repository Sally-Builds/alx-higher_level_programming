#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for op in dir(hidden_4):
        if op[:2] != "__":
            print(op)
