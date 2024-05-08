def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Take user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
for _ in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

