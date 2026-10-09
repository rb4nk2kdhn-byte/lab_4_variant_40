def get_key(number):
    value = abs(number)

    if value == 0:
        return 1

    count = 0
    while value > 0:
        count += 1
        value //= 10

    return count


def prepare_data(numbers):
    return [(number, position) for position, number in enumerate(numbers)]


def insertion_sort(data):
    result = data[:]

    for i in range(1, len(result)):
        current = result[i]
        current_key = get_key(current[0])
        j = i - 1

        
        while j >= 0 and get_key(result[j][0]) < current_key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_key = get_key(left[i][0])
        right_key = get_key(right[j][0])

        
        if left_key >= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data[:]

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    return merge(left, right)


def extract_numbers(data):
    return [number for number, _ in data]


def extract_positions(data):
    return [position for _, position in data]


def find_repeated_keys(sorted_data):
    key_counts = {}

    for number, _ in sorted_data:
        key = get_key(number)
        key_counts[key] = key_counts.get(key, 0) + 1

    # перегляд відсортованих двних зберігає потрібний порядок та всі повтори.
    result = []
    for number, _ in sorted_data:
        if key_counts[get_key(number)] >= 2:
            result.append(number)

    return result


def format_list(values): #повертає список через пробіли або слово 'немає' для пустого списку
    if not values:
        return "немає"

    return " ".join(str(value) for value in values)


def main():
    n = int(input())
    numbers_line = input()  # пустий рядок також читається якщо n == 0  
    numbers = list(map(int, numbers_line.split())) if numbers_line.strip() else []

    original_data = prepare_data(numbers)

    # кожен алгоритм отримує окрему копію початкових даних.
    insertion_result = insertion_sort(original_data[:])
    merge_result = merge_sort(original_data[:])

    insertion_numbers = extract_numbers(insertion_result)
    merge_numbers = extract_numbers(merge_result)
    positions = extract_positions(merge_result)
    repeated_numbers = find_repeated_keys(merge_result)

    print("Вставки:", format_list(insertion_numbers))
    print("Злиття:", format_list(merge_numbers))
    print("Позиції:", format_list(positions))
    print("Повторені:", format_list(repeated_numbers))


if __name__ == "__main__":
    main()
