def to_euro(real_value, rate):
    return real_value * rate
current_rate = 0.16  # Example conversion rate from Real to Euro
user_input = float(input("Enter amount in Real: "))
result = to_euro(user_input, current_rate)
print(f"{user_input} Real is equal to {result:.2f} Euro at the rate of {current_rate}.")
