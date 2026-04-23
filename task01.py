
def calculate(num1: float, num2: float, operator: str) -> float:
    print("Operator tanlang: +, -, *, /: ")
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Nolga bo'lish mumkin emas"
        return round(num1 / num2, 2)

    else:
        return "Error: Noto'g'ri operator"

result = calculate(15, 3, "/")
print("Natija:", result)