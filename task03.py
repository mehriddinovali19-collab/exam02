def calculate_tax(salary: int) -> dict: 
 if salary <= 5_000_000:
   tax_rate = 0
   rate_str = "0%"
 elif salary  <= 10_000_000:
        tax_rate = 0.12
        rate_str = "12%"
 elif salary <= 20_000_000:
     tax_rate = 0.18
     rate_str = "18%"
 else: 
     tax_rate = 0.25
     rate_str = "25%"

 tax = (salary* tax_rate)
 net = salary - tax
 return {"gross": salary,"tax": tax,"net": net,"rate": rate_str}    

print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))
