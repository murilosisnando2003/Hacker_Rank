def split_and_join(line):
    val = line.split(" ")
    val2 = "-".join(val)
    return val2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)