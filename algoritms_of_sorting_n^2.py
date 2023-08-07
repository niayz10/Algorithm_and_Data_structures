

def insert_sort(array:list):
    """ The insert sort algorithm """
    n = len(array)
    for top in range(1, n): # we start from the second element of array
        k = top             # take the index of element 
        while k > 0 and array[k-1] > array[k]: # until the k is greater than 0 and array[k] is greater than array[k-1]
            array[k], array[k-1] = array[k - 1], array[k] # we swap the elements 
            k -= 1 # and decrease the k by 1

def selection_sort(array:list):
    """ The selection sort algoritm """
    n = len(array)
    for pos in range(0, n-1):
        for k in range(pos + 1, n):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
            print(f'array= {array};\n pos= {pos}')


def bubble_sort(array:list):
    """ The bubble sort algoritm """
    n = len(array)
    for i in range(1, n):
        for j in range(n-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def test_alrorithms(func):
    print(f'Testing{func.__doc__}')
    arr = [2, 4, 5, 1, 3]
    sorted_arr = [1, 2, 3, 4, 5]
    func(arr)
    print(f'{arr} sorted' if arr == sorted_arr else 'Failed')



if __name__ == '__main__':
    test_alrorithms(insert_sort)
    test_alrorithms(selection_sort)
    test_alrorithms(bubble_sort)
    