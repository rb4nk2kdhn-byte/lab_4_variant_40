def get_key(number):
    return abs(number - 2)


def prepare_data(numbers):
    return [(number, position) for position, number in enumerate(numbers)]


def insertion_sort_by_key(data):
    result = data[:]

    for i in range(1, len(result)):
        current = result[i]
        current_key = get_key(current[0])
        j = i - 1

        
        while j >= 0 and get_key(result[j][0]) > current_key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


def insertion_sort_positions(positions):
    result = positions[:]

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


def first_key_greater_than(data, threshold):
    left = 0
    right = len(data)

    while left < right:
        middle = (left + right) // 2

        if get_key(data[middle][0]) <= threshold:
            left = middle + 1
        else:
            right = middle

    return left


def linear_search(data, t):
    target_key = None
    positions = []

    # за один прохід визначає найменший ключ більший за t і його позиціх.
    for number, position in data:
        key = get_key(number)

        if key <= t:
            continue

        if target_key is None or key < target_key:
            target_key = key
            positions = [position]
        elif key == target_key:
            positions.append(position)

    return insertion_sort_positions(positions)


def binary_search(sorted_data, t):
    start = first_key_greater_than(sorted_data, t)

    if start == len(sorted_data):
        return []

    target_key = get_key(sorted_data[start][0])
    end = first_key_greater_than(sorted_data, target_key)

    positions = [position for _, position in sorted_data[start:end]]
    return insertion_sort_positions(positions)


def format_list(values):
    if not values:
        return "немає"

    return " ".join(str(value) for value in values)


def main():
    n = int(input())
    numbers_line = input()  # пустий рядок читається якщо n==0 
    numbers = list(map(int, numbers_line.split())) if numbers_line.strip() else []

    data = prepare_data(numbers)
    sorted_data = insertion_sort_by_key(data)  

    q = int(input())

    for _ in range(q):
        t = int(input())
        linear_result = linear_search(data, t)
        binary_result = binary_search(sorted_data, t)

        print("Лінійний:", format_list(linear_result))
        print("Бінарний:", format_list(binary_result))


if __name__ == "__main__":
    main()
