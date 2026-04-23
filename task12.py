def sort_names(students: list) -> list:
    return sorted(students, key= str.lower)

print(sort_names(["Zara", "bobur", "Anvar"]))
