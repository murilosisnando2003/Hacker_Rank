
if __name__ == '__main__':
    n = int(input())
    x = input().split()
    w = input().split()

    # convert values on list in float
    x = [float(i) for i in x]
    w = [float(p) for p in w]

weighted_average = sum(w * x for w, x in zip(w, x)) / sum(w)
 
print(round(weighted_average,1)) # 3.38


   