
def calculate_one_rep_max(weight, rep):
    return weight * (1 + rep / 30)

class GymRatProtocol:
    def __init__(self, weight, rep):
        self.weight = weight
        self.rep = rep
        self.one_rep_max = calculate_one_rep_max(weight, rep)
        self.workout_log = []
    def log_workout(self, exercise, sets, reps, weight):
        workout_entry = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }
        self.workout_log.append(workout_entry)
    def get_one_rep_max(self):
        return self.one_rep_max
    def get_workout_log(self):
        return self.workout_log
    
# Example usage:

# gym_rat = GymRatProtocol(200, 10)
# gym_rat.log_workout("Bench Press", 4, 10, 150)
# gym_rat.log_workout("Squat", 5, 8, 200)
