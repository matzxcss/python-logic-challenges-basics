def aura_counter(word: str) -> dict:
    count = {}
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    return count


print(aura_counter("banana"))


def account_cleaner(list_of_strings: list) -> list:
    cleaned_accounts = []
    for account in list_of_strings:
        cleaned_account = account.replace("$", "").replace(",", "")
        cleaned_accounts.append(float(cleaned_account))
    return cleaned_accounts


print(account_cleaner(["$1,200.50", "$50.00", "$10.25"]))


def candidatos_filter(dictionary: dict) -> list | None:
    filtered_candidates = []
    for candidates in dictionary:
        if candidates["idade"] > 17 and "Python" in candidates["skills"]:
            filtered_candidates.append(candidates)

    return filtered_candidates


candidatos = [
    {"nome": "Matheus", "idade": 18, "skills": ["Python", "Django"]},
    {"nome": "João", "idade": 17, "skills": ["Python"]},
    {"nome": "Cleberson", "idade": 20, "skills": ["JS", "React"]},
]

print(candidatos_filter(candidatos))
