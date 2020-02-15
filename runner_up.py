if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

##best = [x for x in list(arr) if x == n ]

best = set(arr)
best .remove(max(best))

print(max(best)) 
