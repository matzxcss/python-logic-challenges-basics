queue = []
def add_to_queue(passenger_name):
    queue.append(passenger_name)
    return f"{passenger_name} added to the queue."
def serve_next_passenger():
    if queue:
        served_passenger = queue.pop(0)
        return f"{served_passenger} has been served."
    else:
        return "No passengers in the queue."
def view_queue():
    if queue:
        return "Current queue: " + ", ".join(queue)
    else:
        return "The queue is empty."


print(add_to_queue("Matheus"))
print(add_to_queue("Sean"))
print(view_queue())

print("🚌 Bus Arrived!")
print(serve_next_passenger())
print(view_queue())
