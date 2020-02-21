def swap_case(s):
    swapped = []
    for char in s:
        swapped.append(str(char).swapcase())       
    return ''.join(swapped)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)