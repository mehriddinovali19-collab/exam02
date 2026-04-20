def analyze_list(items: list) -> dict:
    total = len(items)

    unique_items = list(set(items))
    unique = len(unique_items)

    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1

    duplicates = []
    for item in items:
        if freq[item] > 1 and item not in duplicates:
            duplicates.append(item)

    most_common = None
    max_count = 0
    for item in items:
        if freq[item] > max_count:
            max_count = freq[item]
            most_common = item

    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common
    }
print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))