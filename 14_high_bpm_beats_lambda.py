meus_beats = {
    "Lofi-Vibe": 85,
    "Trap-Brabo": 140,
    "Melodic-Flow": 120,
    "Dark-Drill": 145,
    "Hyperpop-Energy": 160,
}


def high_bpm_beats() -> dict:
    return {name: bpm for name, bpm in meus_beats.items() if bpm >= 140}


print(high_bpm_beats())

# Saída esperada:
# {'Trap-Brabo': 140, 'Dark-Drill': 145, 'Hyperpop-Energy': 160}
