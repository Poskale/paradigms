import math
from functools import reduce

def mean(arr):
    return sum(arr) / len(arr)

def covariance(arr1, arr2):
    mean1 = mean(arr1)
    mean2 = mean(arr2)
    return sum([(x - mean1) * (y - mean2) for x, y in zip(arr1, arr2)]) / len(arr1)

def std_dev(arr):
    arr_mean = mean(arr)
    return math.sqrt(sum([(x - arr_mean) ** 2 for x in arr]) / len(arr))

def pearson_correlation(arr1, arr2):
    cov = covariance(arr1, arr2)
    std_dev1 = std_dev(arr1)
    std_dev2 = std_dev(arr2)
    return cov / (std_dev1 * std_dev2)

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
correlation = pearson_correlation(array1, array2)
print("Корреляция Пирсона:", correlation)