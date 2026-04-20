def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:
        return "Error: summa manfiy bo'lishi mumkin emas"
    if action == "deposit":
        return balance + amount
    elif action == "withdraw":
        if amount > balance:
            return "Error: balans yetarli emas"
        return balance - amount
    else:
        return "Error: noto'g'ri amal"

print(atm_operation(100000, "deposit", 50000))   
print(atm_operation(100000, "withdraw", 20000))




