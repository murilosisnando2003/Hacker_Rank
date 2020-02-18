from statistics import pstdev,variance

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))

    std = pstdev(x)

    print(round(std,1))
