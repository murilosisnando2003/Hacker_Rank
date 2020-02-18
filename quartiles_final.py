from statistics import median

if __name__ == '__main__':
    n = int(input())
    x = sorted(list(map(int, input().split())))
    
    print(int(median(x[:n//2])))
    print(int(median(x)))
    print(int(median(x[(n+1)//2:])))
