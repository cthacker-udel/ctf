parts = {
    "e": 0,
    "n": 0,
    "c": 0
}

with open("values", "r") as file:
    file.readline()
    for each_line in file.readlines():
        if 'c' in each_line:
            parts["c"] = int(each_line.strip().split("c: ")[1])
        elif 'n' in each_line:
            parts["n"] = int(each_line.strip().split("n: ")[1])
        else:
            parts["e"] = int(each_line.strip().split("e: ")[1])
    x = parts['c'] * parts['e']
    print(x)