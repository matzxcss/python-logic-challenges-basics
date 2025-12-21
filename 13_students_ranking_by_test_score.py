estudantes = [
    ("João Antonio", 85),
    ("João Pedro", 92),
    ("Guilherme", 78),
    ("Matheus", 99),
]

sorted_estudantes = sorted(estudantes, key=lambda estudante: estudante[1], reverse=True)

print("Ranking dos estudantes por nota:")
for i, (nome, nota) in enumerate(sorted_estudantes, start=1):
    print(f"{i}. {nome}: {nota}")


# Saída esperada:
# Ranking dos estudantes por nota:
# 1. Matheus: 99
# 2. João Pedro: 92
# 3. João Antonio: 85
# 4. Guilherme: 78
