import statistics

if __name__ == '__main__':
    n = int(input())
    lista = []
    line = input().split()
    scores = list(map(int, line))
    lista = scores
        

lista.sort()



def find_median(sorted_list):
    indices = []

    list_size = len(sorted_list)
    median = 0

    if list_size % 2 == 0:
        indices.append(int(list_size / 2)-1)  # -1 because index starts from 0
        indices.append(int(list_size / 2))
        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        pass
    else:
        indices.append(int(list_size / 2))

        median = sorted_list[indices[0]]
        pass

    return median, indices
    pass

median, median_indices = find_median(lista)
Q1, Q1_indices = find_median(lista[:median_indices[+1]])
Q2, Q2_indices = find_median(lista[median_indices[0] + 1:])

quartiles = [round(Q1), round(median), round(Q2)]

for items in quartiles:
    print (items)
