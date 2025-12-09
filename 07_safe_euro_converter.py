while True:
    try:
        amount = float(input("Enter amount in Euros: "))
        if amount < 0:
            print("Please enter a non-negative amount.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
