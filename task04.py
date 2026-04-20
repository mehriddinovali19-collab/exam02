def format_name(full_name: str) -> str:
    parts = full_name.split()
    surname = parts[0]
    given_names = parts[1:]
    return " ".join(given_names) + ", " + surname
print(format_name("Aliyev Vali G'aniyevich"))