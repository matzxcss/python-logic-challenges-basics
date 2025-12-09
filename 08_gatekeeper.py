SECRET_PASS = "python123"
user_input = input("Enter the secret password: ")
attempts = 0

while user_input != SECRET_PASS:
    attempts += 1
    if attempts >= 3:
        print("Too many incorrect attempts. Access denied.")
        break
    print("Incorrect password. Try again.")
    user_input = input("Enter the secret password: ")
else:
    print("Access granted. Welcome!")
