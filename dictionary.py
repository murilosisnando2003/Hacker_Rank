if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

newDict = filterTheDict(student_marks, lambda elem : elem[0]==query_name)

avgDict = {}
for k,v in newDict.items():
    # v is the list of grades for student k
    avgDict[k] = sum(v)/ float(len(v))

print("{:.2f}".format(avgDict[query_name]))

