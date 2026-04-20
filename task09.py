def find_min_max(numbers: list) -> dict:
    max_num = max(numbers)
    min_num = min(numbers)
    return {'max number': max_num, 'min number': min_num}
print(find_min_max([3, 7, 10, -55, -8, 15, 22]))