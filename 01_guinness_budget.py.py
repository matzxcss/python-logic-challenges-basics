balance = input("Enter the starting balance:")
balance = float(balance)
cost_per_guinness = 6.5
number_of_guinness = 0

while balance >= cost_per_guinness:
    balance -= cost_per_guinness
    number_of_guinness += 1
    print(f"Purchased Guinness number {number_of_guinness}. Remaining balance: ${balance:.2f}")
