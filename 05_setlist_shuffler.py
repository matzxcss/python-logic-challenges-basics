import random
beat_list = ["cocaine", "de Novo", "asi me gusta", "pack in", "abyss"]
def shuffle_setlist(beats):
    random.shuffle(beats)
    return beats
shuffled_setlist = shuffle_setlist(beat_list)
print("Shuffled Setlist:", shuffled_setlist)
 