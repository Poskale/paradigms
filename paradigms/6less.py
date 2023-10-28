#реализации в императивной парадигме, так как является подходящим выбором благодаря его эффективности, простоте, 
#модификации на месте и совместимости с различными языками программирования.:

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array = [2, 4, 7, 12, 45, 67, 89]
number = 12

result = binary_search(array, number)

if result != -1:
    print(f"Искомый элемент {number} найден в массиве на позиции {result}.")
else:
    print("Искомый элемент не найден.")


# задачи с семинара 
#1 секуномер в императивной парадигме
import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.elapsed_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("Секундомер запущен.")

    def pause(self):
        if self.is_running:
            self.pause_time = time.time()
            self.is_running = False
            print("Секундомер приостановлен.")

    def resume(self):
        if not self.is_running and self.pause_time is not None:
            self.elapsed_time += time.time() - self.pause_time
            self.pause_time = None
            self.is_running = True
            print("Секундомер возобновлен.")

    def stop(self):
        if self.is_running:
            self.elapsed_time += time.time() - self.start_time
            self.is_running = False
        print("Секундомер остановлен.")

    def get_elapsed_time(self):
        if self.is_running:
            return self.elapsed_time + (time.time() - self.start_time)
        else:
            return self.elapsed_time

stopwatch = Stopwatch()
stopwatch.start()

time.sleep(2)  # Пауза на 2 секунды

stopwatch.pause()

time.sleep(3)  # Пауза на 3 секунды

stopwatch.resume()

time.sleep(1)  # Пауза на 1 секунду

stopwatch.stop()

print("Прошло времени:", stopwatch.get_elapsed_time())



#2 Среднеквадратичная ошибка в императивной парадигме
def calculate_mse(predictions, true_values):
    if len(predictions) != len(true_values):
        raise ValueError("Длины векторов не совпадают.")

    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, true_values)]
    mse = sum(squared_errors) / len(predictions)
    return mse

# Пример использования
predictions = [2.5, 3.7, 4.1, 5.0]
true_values = [2.0, 3.5, 4.0, 4.8]

mse = calculate_mse(predictions, true_values)
print("Среднеквадратичная ошибка (MSE):", mse)


#3 Сортировка слиянием в императивной парадигме
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

array = [9, 5, 2, 7, 1, 8, 3, 6, 4]
sorted_array = merge_sort(array)
print("Отсортированный массив:", sorted_array)

