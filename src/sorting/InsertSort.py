def insertSort(array):
    lengthOfArray = len(array)
    for outer in range(1, lengthOfArray):
        pointer = outer - 1
        key = array[outer]
        while pointer >= 0 and array[pointer] > key:
            array[pointer + 1] = array[pointer]
            pointer -= 1
        array[pointer + 1] = key
    return array


if __name__ == '__main__':
    arr = [4, 3, 2, 1]
    print(insertSort(arr))
