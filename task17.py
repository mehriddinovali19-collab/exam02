def filter_positive(numbers: list) -> list:
    result = []
    for num in numbers:
        if num['value'] > 0:
            result.append(num)
    return result

print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))
# [{'value': 10}, {'value': 7}]

print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))
# [{'value': 5}]

