import numpy as np
import statistics

if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        line = input().split()
        scores = list(map(int, line))
        lista = scores

lista.sort()

print(quantiles(lista, n=2))
  
print("arr : ", lista)  
print("Q2 quantile of arr : ", np.quantile(lista, .50)) 
print("Q1 quantile of arr : ", np.quantile(lista, .25)) 
print("Q3 quantile of arr : ", np.quantile(lista, .75)) 
print("100th quantile of arr : ", np.quantile(lista, .1))  
    