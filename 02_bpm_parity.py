bpm_of_beat = input("Enter the BPM of the beat: ")
bpm_of_beat = float(bpm_of_beat)
if bpm_of_beat % 2 == 0:
    print(f"The BPM of {bpm_of_beat} is even.")
else:
    print(f"The BPM of {bpm_of_beat} is odd.")
    