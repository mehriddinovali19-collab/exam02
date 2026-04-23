def find_pattern(items: list, pattern: str, match_type: str) -> list: 
    lower_pattern = pattern.lower()
    result =[]
    for item in items: 
        lower_items = item.lower()
        if match_type == "starts" and lower_items.startswith(lower_pattern):
            result.append(item)
        elif match_type == "ends" and lower_items.endswith(lower_pattern):
            result.append(item)
        elif match_type == "contains" and lower_pattern in lower_items:
            result.append(item)
    return result
print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts"))
print(find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends"))
print(find_pattern(["Python", "Java", "JavaScript"], "java", "contains"))


