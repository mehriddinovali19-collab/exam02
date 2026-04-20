def filter_positive(numbers: list) -> list:
    result = []
    if numbers > 0:
        result.append(numbers)
    return result
print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))