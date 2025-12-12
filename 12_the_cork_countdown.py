from datetime import datetime, timedelta
def cork_countdown(event_date):
    """
    Calculate the number of days remaining until the specified event date.

    Parameters:
    event_date (str): The date of the event in 'YYYY-MM-DD' format.

    Returns:
    int: Number of days remaining until the event.
    """
    today = datetime.now().date()
    event = datetime.strptime(event_date, '%Y-%m-%d').date()
    delta = event - today
    return delta.days
# Example usage:
# days_remaining = cork_countdown('2024-12-31')
# print(f"Days remaining until the event: {days_remaining} days")
# Output will vary depending on the current date
# Example usage:
# days_remaining = cork_countdown('2024-12-31')
# print(f"Days remaining until the event: {days_remaining} days")
# Output will vary depending on the current date
