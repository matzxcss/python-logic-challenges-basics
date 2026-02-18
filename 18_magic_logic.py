from string import punctuation


def pass_validator(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in punctuation for char in password):
        return False
    return True


print(pass_validator("Password123!"))  # True
print(pass_validator("password"))  # False


vendas = [
    {"produto": "Teclado", "categoria": "TI", "valor": 200.0},
    {"produto": "Monitor", "categoria": "TI", "valor": 1000.0},
    {"produto": "Cadeira", "categoria": "Moveis", "valor": 500.0},
    {"produto": "Mouse", "categoria": "TI", "valor": 100.0},
]

# expected {'TI': 1300.0, 'Moveis': 500.0}


def total_sellings(sellings: list) -> dict:
    total = {}
    for selling in sellings:
        category = selling["categoria"]
        value = selling["valor"]
        if category in total:
            total[category] += value
        else:
            total[category] = value
    return total


print(total_sellings(vendas))


def twins_detector(lista: list, target: int) -> list:
    twins = []
    visiteds = {}
    for i, num in enumerate(lista):
        complement = target - num
        if complement in visiteds:
            twins.append((visiteds[complement], i))
        visiteds[num] = i
    return twins


print(twins_detector([1, 2, 3, 4, 5], 5))  # [(0, 3), (1, 2)]
