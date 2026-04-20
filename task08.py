def calculate_stats(numbers: list) -> dict:
    total = sum(numbers)
    average = round(total / len(numbers), 2) if numbers else 0.0
    return {
        "sum": total,
        "average": average}

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
print(calculate_stats([10, 20, 30]))
