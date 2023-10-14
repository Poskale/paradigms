def sort_list_imperative(numbers):
    # Используем алгоритм сортировки выбором
    n = len(numbers)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    return numbers

numbers = [5, 2, 9, 1, 7]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers2 = [5, 2, 9, 1, 7]
sorted_numbers = sort_list_declarative(numbers2)
print(sorted_numbers)  
