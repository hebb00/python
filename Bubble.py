def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":

    print("sorted", BubbleSort([7,5,9,3,4,0]))
