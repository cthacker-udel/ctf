with open("./lvl1.txt") as file:
    l = file.readline()
    x = len(l)
    _bytes = []
    for i in range(0, len(l), 8):
        _bytes.append(l[i: i + 8])
    print(_bytes)
    converted_bytes = [int(bite, 2) for bite in _bytes]
    char_ = [chr(x) for x in converted_bytes]
    print(char_)