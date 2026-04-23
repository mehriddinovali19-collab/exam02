def format_name(full_name: str) -> str:
    parts = full_name.split()
    surname = parts[0]
    given_name = parts[1:]

    return " ".join(given_name) + " " + surname
print(format_name("Aliyev Vali G'aniyevich"))