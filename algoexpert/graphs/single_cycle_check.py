# Time Complexity - O(n)
# Space Complexity - O(1)
def hasSingleCycle(array):
    starting_index = 0
    current_index = (starting_index + array[starting_index]) % len(array)

    while True:
        if array[current_index] is None:
            return False

        if current_index == starting_index:
            break
        else:
            val = array[current_index]
            array[current_index] = None

        new_index = (current_index + val) % len(array)
        current_index = new_index

    array[starting_index] = None
    for elem in array:
        if elem is not None:
            return False

    return True


def main():
    array = [2, 3, 1, -4, -4, 2]
    result = hasSingleCycle(array)
    print(result)


if __name__ == '__main__':
    main()
