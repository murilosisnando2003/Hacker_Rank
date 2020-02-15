from statistics import mode

if __name__ == '__main__':
    n = int(input())
    line = input().split()
    scores = list(map(float, line))
   
    #media
    media = sum(scores)/ float(n)
    print(media)
    #median
    scores.sort()
    if n % 2 == 0:
        median1 = scores[n//2]
        median2 = scores[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = scores[n//2]
    print(median)

    #mode
    # data = Counter(scores)
    # get_mode = dict(data)
    # mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    # if len(mode) == n: 
    #     get_mode = "No mode found"
    # else: 
    #     get_mode = "Mode is / are: " + ', '.join(map(str, mode))   
    moda = max(scores, key = scores.count)
    #mode(scores)
    print(moda) 



